import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# ==============================
# Load environment variables
# ==============================
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")
model_name = os.getenv("MODEL_NAME")

# ==============================
# Initialize LLM
# ==============================
llm = ChatOpenAI(
    model=model_name,
    temperature=0.7,
    max_tokens=500,  # type: ignore
    api_key=api_key,
    base_url=base_url
)

# ==============================
# Prompt template
# ==============================
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

chain = prompt | llm

def generate_post(topic: str, language: str) -> str:
    """Generates a LinkedIn post using the LLM."""
    result = chain.invoke({"topic": topic, "language": language})
    return result.content

# ==============================
# Streamlit UI
# ==============================
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="📝", layout="wide")

# Sidebar
with st.sidebar:
    st.header("Settings ⚙️")
    language = st.selectbox("Choose language:", ["English", "Bengali", "Spanish"])
    st.markdown("---")
    st.markdown("Made with ❤️ using **LangChain + GitHub Models**")

# Main content
st.title("📝 LinkedIn Post Generator (AI Agent)")
st.markdown("Generate professional LinkedIn posts instantly.")

# Session state for topic and post
if "topic" not in st.session_state:
    st.session_state.topic = ""
if "post" not in st.session_state:
    st.session_state.post = ""

# Input
st.session_state.topic = st.text_input("Enter your topic here:", value=st.session_state.topic)

# Buttons
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Generate Post"):
        if st.session_state.topic.strip():
            with st.spinner("Generating your LinkedIn post..."):
                st.session_state.post = generate_post(st.session_state.topic, language)
            st.success("✅ Post generated successfully!")
        else:
            st.warning("⚠️ Please enter a topic first.")

with col2:
    if st.button("Refresh"):
        st.session_state.topic = ""
        st.session_state.post = ""
        st.experimental_rerun()  # Refresh the page

# Display generated post
if st.session_state.post:
    st.markdown("### ✍️ Generated LinkedIn Post:")
    st.text_area("Post Content", st.session_state.post, height=250)