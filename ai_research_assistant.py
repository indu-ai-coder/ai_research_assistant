"""
AI Research Assistant
A tool to help with research tasks using LangChain, OpenAI, and web scraping
"""

import os
from typing import List, Optional
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from bs4 import BeautifulSoup
import requests

# Load environment variables from .env file
load_dotenv()


class AIResearchAssistant:
    """AI-powered research assistant for gathering and analyzing information."""
    
    def __init__(self, openai_api_key: Optional[str] = None):
        """
        Initialize the AI Research Assistant.
        
        Args:
            openai_api_key: OpenAI API key. If None, will use OPENAI_API_KEY env variable.
        """
        self.api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided or set in OPENAI_API_KEY environment variable")
        
        self.embeddings = OpenAIEmbeddings(openai_api_key=self.api_key)
        self.llm = ChatOpenAI(temperature=0, openai_api_key=self.api_key)
        self.vectorstore = None
        self.qa_chain = None
    
    def scrape_url(self, url: str) -> str:
        """
        Scrape content from a URL.
        
        Args:
            url: The URL to scrape
            
        Returns:
            Extracted text content from the URL
        """
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text
            text = soup.get_text()
            
            # Clean up text
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            
            return text
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            return ""
    
    def create_vectorstore(self, documents: List[str], chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Create a FAISS vectorstore from documents.
        
        Args:
            documents: List of text documents
            chunk_size: Size of text chunks
            chunk_overlap: Overlap between chunks
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        texts = []
        for doc in documents:
            texts.extend(text_splitter.split_text(doc))
        
        self.vectorstore = FAISS.from_texts(texts, self.embeddings)
        
        # Create QA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever()
        )
        
        print(f"Vectorstore created with {len(texts)} text chunks")
    
    def ask_question(self, question: str) -> str:
        """
        Ask a question based on the loaded documents.
        
        Args:
            question: The question to ask
            
        Returns:
            The answer from the QA chain
        """
        if not self.qa_chain:
            return "No documents loaded. Please create a vectorstore first."
        
        result = self.qa_chain.run(question)
        return result
    
    def save_vectorstore(self, path: str):
        """Save the vectorstore to disk."""
        if self.vectorstore:
            self.vectorstore.save_local(path)
            print(f"Vectorstore saved to {path}")
        else:
            print("No vectorstore to save")
    
    def load_vectorstore(self, path: str):
        """Load a vectorstore from disk."""
        self.vectorstore = FAISS.load_local(path, self.embeddings)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever()
        )
        print(f"Vectorstore loaded from {path}")


def main():
    """Main function to demonstrate the AI Research Assistant."""
    print("AI Research Assistant")
    print("=" * 50)
    
    # Initialize the assistant
    try:
        assistant = AIResearchAssistant()
        print("✓ Assistant initialized successfully")
    except ValueError as e:
        print(f"Error: {e}")
        print("\nPlease set your OpenAI API key:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return
    
    # Example usage
    print("\nExample: Scraping a URL and creating a knowledge base")
    print("-" * 50)
    
    # You can add your own URLs here
    urls = [
        # "https://example.com/article1",
        # "https://example.com/article2",
    ]
    
    if urls:
        documents = []
        for url in urls:
            print(f"Scraping: {url}")
            content = assistant.scrape_url(url)
            if content:
                documents.append(content)
        
        if documents:
            print(f"\nCreating vectorstore from {len(documents)} documents...")
            assistant.create_vectorstore(documents)
            
            # Example questions
            questions = [
                "What is the main topic discussed?",
                "Summarize the key points.",
            ]
            
            for question in questions:
                print(f"\nQ: {question}")
                answer = assistant.ask_question(question)
                print(f"A: {answer}")
    else:
        print("No URLs provided. Add URLs to the 'urls' list to test the assistant.")


if __name__ == "__main__":
    main()
