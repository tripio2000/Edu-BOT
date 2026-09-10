from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

def get_api_key():
    """
    Loads the LLM API key from the .env file and returns it.
    
    Raises:
        ValueError: If the LLM_API_KEY is not found in the environment.
        
    Returns:
        str: The LLM API key.
    """
    # This line loads the environment variables from the .env file
    load_dotenv()
    
    # os.getenv() retrieves the value of the environment variable
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # This is a critical security and robustness check
    if not api_key:
        raise ValueError("API Key not found. Make sure you have a .env file with LLM_API_KEY defined.")
        
    return api_key

def LoadGoogleLLM():
    """Instantiates and returns a Google LLM through the LangChain interface."""
    # Ensure your GOOGLE_API_KEY is set as an environment variable
    llm = ChatGoogleGenerativeAI(model="gemma-4-31b-it", temperature=0)
    return llm

