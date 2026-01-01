# ai_research_assistant
Gen AI Research Assistant using LangChain, Open AI, FAISS CPU

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure OpenAI API Key:**
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and replace `your_openai_api_key_here` with your actual OpenAI API key:
     ```
     OPENAI_API_KEY=sk-your-actual-api-key-here
     ```

3. **Run the assistant:**
   ```bash
   python ai_research_assistant.py
   ```

## Security Note

Never commit your `.env` file to version control. The `.gitignore` file is configured to exclude it automatically.

