from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
import numpy as np

def process_markdown_document(file_path):
    """Loads a Markdown document and returns a LangChain Document object.

    Args:
        file_path (str): The path to the Markdown file.

    Returns:
        langchain.document_loaders.TextLoader: A TextLoader object containing the document.
    """

    loader = TextLoader(file_path,encoding="UTF8")
    documents = loader.load()

    # Split documents by Markdown sections
    headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
    ("####", "Header 4"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=True)
    md_header_splits = markdown_splitter.split_text(documents[0].page_content)
    return md_header_splits

# Helper function for printing docs
def pretty_print_docs(docs):
    print(
        f"\n{'-' * 100}\n".join(
            [f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]
        )
    )
    
def EmbeddDocsAndPersist(all_splits,embedding_encoder,PERSIST_DIRECTORY):
    # Crear embeddings y persistir la DB en disco
    # Esto solo se hace una vez o cuando los documentos cambian
    print("Creando y persistiendo la base de datos de vectores...")
    vectorStore = Chroma.from_documents(
        documents=all_splits,
        embedding=embedding_encoder,
        persist_directory=PERSIST_DIRECTORY
    )
    print("Base de datos creada y guardada.")
    return vectorStore

def load_persisted_db(embedding_encoder,PERSIST_DIRECTORY):
    # Cargar la DB desde el disco
    print("Cargando base de datos persistente...")
    vectorStore = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embedding_encoder
    )
    print("Base de datos cargada.")
    return vectorStore

#Define a function for joining retrieved chunks
def join_docs(docs):
    return "\n".join(doc.page_content for doc in docs)
    
    
def evaluate_vectorstore_as_retriever(eval_dataset, vector_store, k=5):
    """
    Evaluates the performance of a retriever using a given dataset.

    Args:
        eval_dataset (list): A list of dictionaries with "question" and "ground_truth_doc_id".
        vector_store: The ChromaDB vector store instance.
        k (int): The number of top documents to retrieve for evaluation.

    Returns:
        dict: A dictionary containing the calculated metrics.
    """
    hits = 0
    reciprocal_ranks = []
    misses = [] # To store information about failed queries for later analysis

    print(f"Starting evaluation for k={k}...")

    for item in eval_dataset:
        question = item["question"]
        ground_truth_id = item["ground_truth_doc_id"]
        
        # Perform the similarity search
        # The result is a list of tuples: [(Document, score), (Document, score), ...]
        retrieved_docs_with_scores = vector_store.similarity_search_with_score(question, k=k)
        
        # Extract the doc_ids from the metadata of the retrieved documents
        retrieved_ids = [doc.metadata.get('doc_id') for doc, score in retrieved_docs_with_scores]
        
        # Check if the ground truth ID is in the retrieved IDs
        if ground_truth_id in retrieved_ids:
            hits += 1
            # Find the rank (position) of the correct document. Ranks are 1-based.
            rank = retrieved_ids.index(ground_truth_id) + 1
            reciprocal_ranks.append(1 / rank)
        else:
            reciprocal_ranks.append(0)
            misses.append({
                "question": question,
                "expected": ground_truth_id,
                "retrieved": retrieved_ids
            })

    total_questions = len(eval_dataset)
    hit_rate = (hits / total_questions) * 100
    mrr = np.mean(reciprocal_ranks)

    return {
        "hit_rate_at_k": k,
        "hit_rate": f"{hit_rate:.2f}%",
        "mrr": f"{mrr:.4f}",
        "total_questions": total_questions,
        "hits": hits,
        "misses_count": len(misses),
        "misses": misses
    }
