import os
import sys
from dotenv import load_dotenv
from langchain_openai import OpenAI
from bs4 import BeautifulSoup
import requests

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI model
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")

openai_model = OpenAI(temperature=0.7, openai_api_key=api_key)

# Gather information
def gather_information(topic):
    """
    Scrape information from Wikipedia about a given topic.
    
    Args:
        topic: The Wikipedia topic to search for
        
    Returns:
        Extracted text content from Wikipedia
    """
    try:
        url = f"https://en.wikipedia.org/wiki/{topic}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([para.text for para in paragraphs])
        return text
    except requests.RequestException as e:
        print(f"Error fetching information for topic '{topic}': {str(e)}")
        return ""

# Analyse information
def analyze_information(text):
    """
    Analyze and summarize text using OpenAI.
    
    Args:
        text: The text to analyze
        
    Returns:
        A summary and analysis of the text
    """
    if not text:
        return "No text to analyze."
    
    try:
        # Create a prompt for summarization and analysis
        prompt = f"""Please provide a comprehensive summary and analysis of the following text:

{text[:4000]}  # Limit text length to avoid token limits

Provide:
1. A concise summary (2-3 sentences)
2. Key points and main topics
3. Any interesting insights
"""
        
        summary = openai_model.invoke(prompt)
        return summary
    except Exception as e:
        print(f"Error analyzing information: {str(e)}")
        return "Error occurred during analysis."

# Running the research Assistant
if __name__ == "__main__":
    # Get topic from command line argument or use default
    if len(sys.argv) > 1:
        topic = sys.argv[1]
    else:
        topic = input("Enter the topic to research (e.g., Artificial_intelligence): ").strip()
        if not topic:
            print("No topic provided. Exiting.")
            sys.exit(1)
    
    print(f"Gathering information about: {topic}")
    info = gather_information(topic)
    
    if info:
        print(f"\nGathered {len(info)} characters of text.")
        print("\nAnalyzing information...\n")
        analysis = analyze_information(info)
        
        # Display results
        print("="*50)
        print("ANALYSIS RESULTS:")
        print("="*50)
        print(analysis)
        
        # Write results to file
        output_filename = f"{topic}_analysis.txt"
        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(f"Topic: {topic}\n")
                f.write("="*50 + "\n")
                f.write(f"Gathered {len(info)} characters of text.\n\n")
                f.write("ANALYSIS RESULTS:\n")
                f.write("="*50 + "\n\n")
                f.write(str(analysis))
            print(f"\n✓ Results saved to: {output_filename}")
        except Exception as e:
            print(f"\nError saving to file: {str(e)}")
    else:
        print("Failed to gather information. Please check the topic name and try again.")