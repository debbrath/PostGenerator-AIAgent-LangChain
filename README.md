# 📝 LinkedIn Post Generator (AI Agent)

A web-based AI tool that generates professional LinkedIn posts using **LangChain** and **GitHub-hosted OpenAI models**. Users can input a topic and select a language, and the AI will produce a polished LinkedIn post ready to share.

---

## Features

- Generate LinkedIn posts in multiple languages: English, Bengali, Spanish.
- Posts are professional, engaging, and 2–4 paragraphs long.
- Modern Streamlit-based user interface.
- Supports GitHub-hosted OpenAI models for AI inference.
- Lightweight and easy to run locally with Python.

---

## Project Structure
```
PostGenerator-AIAgent-LangChain/
│
├─ Venv/ # Python virtual environment
├─ Main.py # CLI version of LinkedIn post generator
├─ UI.py # Streamlit-based web UI
├─ requirements.txt # Python dependencies
├─ .env # Environment variables (API keys, model info)
├─ README.md # Project documentation


```
---

## Installation

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd PostGenerator-AIAgent-LangChain
Create a virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Setup environment variables

Create a .env file in the project root:

env
Copy code
OPENAI_API_KEY="your_openai_api_key"
OPENAI_BASE_URL="https://models.github.ai/inference"   # GitHub Models endpoint
MODEL_NAME="openai/gpt-4.1"
Usage
CLI Version
Run Main.py:

bash
Copy code
python Main.py
Enter the topic.

Choose the language.

The generated LinkedIn post will appear in the terminal.

Streamlit Web UI
Run UI.py:

bash
Copy code
streamlit run UI.py
Open the provided local URL (usually http://localhost:8501).

Enter your topic and select a language.

Click Generate Post to receive your AI-generated LinkedIn post.

Dependencies
LangChain – Chain AI prompts and models.

OpenAI – LLM inference.

Python-dotenv – Manage environment variables.

Streamlit – Web-based user interface.

Screenshots
Add screenshots here of your Streamlit UI or CLI output.

License
MIT License © 2025
Made with ❤️ using LangChain + GitHub Models.

Future Improvements
Add support for more languages.

Add LinkedIn post formatting options.

Save generated posts to a local database or CSV.

Add scheduling for auto-posting on LinkedIn.

pgsql
Copy code

I can also create a **shorter, “GitHub-ready” version with badges and installation buttons** if you want it to look more professional for a repository.  

Do you want me to do that?




# PostGenerator-AIAgent-LangChain
Using ChatGPT, AI Agent for generating LinkedIn Posts with LangChain


Open a terminal in the folder and run:
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

pip install -r requirements.txt



python -m main.py
streamlit run UI.py
