"""
AI Research Assistant - Step by Step Implementation
Follow the steps below to build your AI Research Assistant
"""

import os
from typing import List, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Step 1: Import necessary libraries
# TODO: Uncomment these imports as you progress through the steps
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.vectorstores import FAISS
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import RetrievalQA
# from bs4 import BeautifulSoup
# import requests


# ============================================================================
# STEP 2: Create the AIResearchAssistant class
# ============================================================================

class AIResearchAssistant:
    """AI-powered research assistant for gathering and analyzing information."""
    
    def __init__(self, openai_api_key: Optional[str] = None):
        """
        STEP 2.1: Initialize the AI Research Assistant.
        
        TODO:
        1. Store the API key (from parameter or environment variable)
        2. Raise ValueError if no API key is found
        3. Initialize OpenAI embeddings
        4. Initialize ChatOpenAI LLM with temperature=0
        5. Set vectorstore and qa_chain to None initially
        """
        pass
    
    
    # ========================================================================
    # STEP 3: Implement web scraping
    # ========================================================================
    
    def scrape_url(self, url: str) -> str:
        """
        STEP 3.1: Scrape content from a URL using BeautifulSoup.
        
        TODO:
        1. Make a GET request to the URL with timeout=10
        2. Parse the HTML with BeautifulSoup
        3. Remove script and style tags
        4. Extract and clean the text
        5. Handle exceptions and return empty string on error
        
        Args:
            url: The URL to scrape
            
        Returns:
            Extracted text content from the URL
        """
        pass
    
    
    # ========================================================================
    # STEP 4: Implement vectorstore creation
    # ========================================================================
    
    def create_vectorstore(self, documents: List[str], chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        STEP 4.1: Create a FAISS vectorstore from documents.
        
        TODO:
        1. Create a RecursiveCharacterTextSplitter with given chunk_size and chunk_overlap
        2. Split all documents into chunks
        3. Create FAISS vectorstore from texts using embeddings
        4. Create a RetrievalQA chain with the vectorstore
        5. Print confirmation message with number of chunks
        
        Args:
            documents: List of text documents
            chunk_size: Size of text chunks
            chunk_overlap: Overlap between chunks
        """
        pass
    
    
    # ========================================================================
    # STEP 5: Implement question answering
    # ========================================================================
    
    def ask_question(self, question: str) -> str:
        """
        STEP 5.1: Ask a question based on the loaded documents.
        
        TODO:
        1. Check if qa_chain exists
        2. If not, return error message
        3. Run the question through the qa_chain
        4. Return the result
        
        Args:
            question: The question to ask
            
        Returns:
            The answer from the QA chain
        """
        pass
    
    
    # ========================================================================
    # STEP 6: Implement save/load functionality
    # ========================================================================
    
    def save_vectorstore(self, path: str):
        """
        STEP 6.1: Save the vectorstore to disk.
        
        TODO:
        1. Check if vectorstore exists
        2. If yes, save it to the given path
        3. Print confirmation message
        """
        pass
    
    def load_vectorstore(self, path: str):
        """
        STEP 6.2: Load a vectorstore from disk.
        
        TODO:
        1. Load FAISS vectorstore from path using embeddings
        2. Create a new RetrievalQA chain with loaded vectorstore
        3. Print confirmation message
        """
        pass


# ============================================================================
# STEP 7: Implement the main function
# ============================================================================

def main():
    """
    STEP 7.1: Create a main function to test the assistant.
    
    TODO:
    1. Print welcome message
    2. Initialize the AIResearchAssistant
    3. Handle ValueError if API key is missing
    4. Define a list of URLs to scrape
    5. Scrape each URL and collect documents
    6. Create vectorstore from documents
    7. Ask sample questions
    8. Print questions and answers
    """
    print("AI Research Assistant - Step by Step")
    print("=" * 50)
    
    # TODO: Implement the main logic here
    pass


# ============================================================================
# STEP 8: Test your implementation
# ============================================================================

if __name__ == "__main__":
    # Before running, make sure to:
    # 1. Set your OpenAI API key: export OPENAI_API_KEY='your-key'
    # 2. Uncomment the imports at the top
    # 3. Implement all the TODO sections
    
    print("\n" + "=" * 50)
    print("IMPLEMENTATION CHECKLIST:")
    print("=" * 50)
    print("[ ] Step 1: Uncomment imports")
    print("[ ] Step 2: Implement __init__ method")
    print("[ ] Step 3: Implement scrape_url method")
    print("[ ] Step 4: Implement create_vectorstore method")
    print("[ ] Step 5: Implement ask_question method")
    print("[ ] Step 6: Implement save/load methods")
    print("[ ] Step 7: Implement main function")
    print("[ ] Step 8: Set OpenAI API key and test")
    print("=" * 50 + "\n")
    
    # Uncomment this when ready to test:
    # main()
