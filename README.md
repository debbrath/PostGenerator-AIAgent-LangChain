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

## Technologies

- Python 3.10+

- Streamlit

- langchain


## ⚙️ Installation

### 1. Install Python and VS Code

Make sure you have Python 3.10+ installed.

Install VS Code and open the project folder.

### 2. Clone the repository

```bash
git clone <your-repo-url>
cd PostGenerator-AIAgent-LangChain
Create a virtual environment

```
###  3.	Open VS Code
	Create a new folder named PostGenerator-AIAgent-LangChain.

### 4. Copy API Key

Copy code
OPENAI_API_KEY="your_openai_api_key"
OPENAI_BASE_URL="https://models.github.ai/inference"   # GitHub Models endpoint
MODEL_NAME="openai/gpt-4.1"

### 5. Create a virtual environment 
    Open a terminal in the folder and run:
    python -m venv venv
    source venv/bin/activate       # Linux/macOS
    venv\Scripts\activate          # Windows

### 6.  Install dependencies:

    pip install -r requirements.txt

### 7. Run 

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

### 8. Dependencies
LangChain – Chain AI prompts and models.

OpenAI – LLM inference.

Python-dotenv – Manage environment variables.

Streamlit – Web-based user interface.


---

## 📸 Screenshots

![Screenshot](https://github.com/debbrath/PostGenerator-AIAgent-LangChain/blob/main/image/LinkedInPost_1.png)


---


✍️ Author

Debbrath Debnath

📫 [Connect on LinkedIn](https://www.linkedin.com/in/debbrathdebnath/)

🌐 [GitHub Profile](https://github.com/debbrath)
