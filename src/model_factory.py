import os
from abc import ABC, abstractmethod
from typing import Optional


# =====================================================================
# 1. ESTRATEGIAS DE CARGA (Single Responsibility & Open/Closed)
# =====================================================================

class BaseLLMProvider(ABC):
    """Interfaz base para proveedores de LLM."""
    
    @abstractmethod
    def load(self):
        pass


class GeminiProvider(BaseLLMProvider):
    """Carga de modelos Google Gemini vía API."""
    
    def __init__(self, model_name: Optional[str] = None, temperature: float = 0.0):
        self.model_name = model_name or os.getenv("GOOGLE_MODEL", "gemma-3-27b-it")
        self.temperature = temperature

    def load(self):
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        return ChatGoogleGenerativeAI(
            model=self.model_name,
            temperature=self.temperature
        )


class LlamaCPPProvider(BaseLLMProvider):
    """Carga de modelos locales GGUF mediante llama.cpp."""
    
    def __init__(self, model_path: Optional[str] = None, n_ctx: int = 4096):
        default_path = os.path.expanduser(
#            "~/.cache/llama.cpp/unsloth_gemma-3-270m-it-qat-GGUF_gemma-3-270m-it-qat-Q4_K_M.gguf"
             "~/.cache/llama.cpp/unsloth_Llama-3.2-1B-Instruct-GGUF_Llama-3.2-1B-Instruct-Q4_K_M.gguf"           
        )
        self.model_path = model_path or os.getenv("LLAMACPP_MODEL_PATH", default_path)
        self.n_ctx = n_ctx

    def load(self):
        from langchain_community.llms import LlamaCpp
        
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"No se encontró el archivo del modelo en: {self.model_path}")
        
        return LlamaCpp(
            model_path=self.model_path,
            n_ctx=self.n_ctx,
            temperature=1.0
        )


# =====================================================================
# 2. FABRICA DE MODELOS (KISS & Dependency Inversion)
# =====================================================================

class ModelFactory:
    """Fábrica para instanciar el modelo (Gemini o LlamaCPP)."""
    
    _PROVIDERS = {
        "gemini": GeminiProvider,
        "llamacpp": LlamaCPPProvider,
    }

    @classmethod
    def create_model(cls, provider: str, **kwargs):
        provider_key = provider.lower()
        if provider_key not in cls._PROVIDERS:
            raise ValueError(
                f"Proveedor '{provider}' no válido. Opciones: {list(cls._PROVIDERS.keys())}"
            )
        
        return cls._PROVIDERS[provider_key](**kwargs).load()
