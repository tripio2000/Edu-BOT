import os
from pathlib import Path
from typing import List, Optional

from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import LlamaCppEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter


class VectorStoreManager:
    """Maneja la carga de documentos, fragmentación y creación de la BD vectorial."""

    def __init__(
        self,
        embedding_model_path: Optional[str] = None,
        persist_directory: str = "./db_chroma",
        n_ctx: int = 8192,
        n_gpu_layers: int = 0
    ):
        self.persist_directory = persist_directory
        default_model_path = os.path.expanduser("~/.cache/llama.cpp/nomic-embed-text-v2-moe.Q6_K.gguf")
        model_path = embedding_model_path or os.getenv("EMBEDDING_MODEL_PATH", default_model_path)

        # Inicialización del encoder de Embeddings
        self.embeddings = LlamaCppEmbeddings(
            model_path=model_path,
            n_gpu_layers=n_gpu_layers,
            n_batch=64,
            n_ctx=n_ctx,
            verbose=False
        )

    def process_markdown(self, file_path: str) -> List[Document]:
        """Carga un archivo Markdown y lo divide según sus encabezados."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

        loader = TextLoader(file_path, encoding="utf-8")
        documents = loader.load()

        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
            ("####", "Header 4"),
        ]
        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on,
            strip_headers=True
        )
        
        return markdown_splitter.split_text(documents[0].page_content)

    def create_and_persist_db(self, documents: List[Document]) -> Chroma:
        """Genera embeddings y persiste la base de datos en disco."""
        print(f"Persistiendo {len(documents)} fragmentos en '{self.persist_directory}'...")
        vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        print("Base de datos vectorial creada con éxito.")
        return vector_store


class RAGRetriever:
    """Maneja las consultas a la BD vectorial y la reordenación (Reranking) de resultados."""

    def __init__(
        self,
        embeddings: LlamaCppEmbeddings,
        persist_directory: str = "./db_chroma",
        reranker_model_name: str = "BAAI/bge-reranker-v2-m3"
    ):
        if not os.path.exists(persist_directory):
            raise FileNotFoundError(f"La BD vectorial no existe en: {persist_directory}")

        self.vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings
        )
        self.reranker_model_name = reranker_model_name
        self._reranker = None

    @property
    def reranker(self):
        """Carga diferida (Lazy loading) del Reranker solo cuando se necesita."""
        if self._reranker is None:
            from langchain_community.cross_encoders import HuggingFaceCrossEncoder
            self._reranker = HuggingFaceCrossEncoder(model_name=self.reranker_model_name)
        return self._reranker

    def retrieve(self, query: str, top_k: int = 5, use_reranker: bool = False) -> List[Document]:
        """Recupera los documentos más relevantes para una consulta."""
        if not use_reranker:
            return self.vector_store.similarity_search(query, k=top_k)

        # Recuperar más candidatos si se va a aplicar reranking
        initial_docs = self.vector_store.similarity_search(query, k=top_k * 2)
        if not initial_docs:
            return []

        # Preparar pares (query, texto) para el reranker
        pairs = [[query, doc.page_content] for doc in initial_docs]
        scores = self.reranker.score(pairs)

        # Ordenar documentos por el score asignado por el CrossEncoder
        scored_docs = sorted(zip(scores, initial_docs), key=lambda x: x[0], reverse=True)
        return [doc for _, doc in scored_docs[:top_k]]

    @staticmethod
    def format_docs(docs: List[Document]) -> str:
        """Une el contenido de los documentos recuperados en una cadena de texto."""
        return "\n\n".join(doc.page_content for doc in docs)
