import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


# Load API keys from .env
load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
model_name = os.getenv("MODEL_NAME")



# Initialize model (using GitHub models "gpt-4.1-nano")
llm = ChatOpenAI(
    model=model_name,
    temperature=0.7,
    max_tokens=500, # type: ignore
    api_key=api_key,       
    base_url=base_url
)


# Prompt template for LinkedIn post generation
template = """
You are a professional LinkedIn content writer.
Write a LinkedIn post about the topic: "{topic}".
The post should be written in {language}, professional, engaging, and 2–4 paragraphs long.
Do not use hashtags or emojis unless necessary.
"""

prompt = PromptTemplate(
    input_variables=["topic", "language"],
    template=template,
)


# Modern runnable chain
chain = prompt | llm


# === Example Run ===
def generate_post(topic, language):
    result = chain.invoke({"topic": topic, "language": language})
    return result.content

if __name__ == "__main__":
    topic = input("Enter topic: ").strip()
    language = input("Language [English/Bengali/Spanish]: ").strip().title()

    post = generate_post(topic, language)
    print("\nGenerated LinkedIn Post:\n")
    print(post)
