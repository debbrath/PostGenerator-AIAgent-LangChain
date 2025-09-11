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
# Streamlit UI Layout
# ==============================
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="📝", layout="wide")

# ==============================
# Top Banner
# ==============================
st.markdown(
    """
    <style>
    .top-banner {
        width: 100%;
        background: linear-gradient(90deg, #4CAF50, #45a049);
        padding: 15px 0; 
        text-align: center;
        border-radius: 0px 0px 10px 10px; 
        color: white;
        font-size: 24px; 
        font-weight: 600;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.15);
        position: fixed;
        top: 0;
        left: 0;
        z-index: 9999;
    }
    .top-banner-sub {
        font-size: 14px;
        font-weight: 400;
        margin-top: 2px;
        opacity: 0.9;
    }
    .stApp {
        margin-top: 110px;
        margin-left: 50px;
        margin-right: 50px;
    }
    textarea {
        width: 100% !important;
    }
    </style>
    <div class="top-banner">
        📝 LinkedIn Post Generator
        <div class="top-banner-sub">
        Generate professional posts instantly with AI
        </div>
        <div class="top-banner-sub">
        Made with ❤️ using <b>LangChain + GitHub Models</b>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ==============================
# Left-Right Layout
# ==============================
left_col, right_col = st.columns([1, 2])  # Left narrower, right wider

# ------------------------------
# Left Column: Inputs
# ------------------------------
with left_col:
    st.subheader("🖊️ Enter Your Topic & Settings")

    # Language selector
    language = st.selectbox("Choose language:", ["English", "Bengali", "Spanish"])

    # Topic input
    if "topic" not in st.session_state:
        st.session_state.topic = ""
    st.session_state.topic = st.text_input("Topic:", value=st.session_state.topic)

    # Action buttons
    if st.button("Generate Post"):
        if st.session_state.topic.strip():
            with st.spinner("Generating your LinkedIn post..."):
                st.session_state.post = generate_post(st.session_state.topic, language)
            st.success("✅ Post generated successfully!")
        else:
            st.warning("⚠️ Please enter a topic first.")

    if st.button("Refresh"):
        for key in ["topic", "post"]:
            if key in st.session_state:
                del st.session_state[key]
        st.success("✅ Cleared!")

# ------------------------------
# Right Column: Output
# ------------------------------
with right_col:
    st.subheader("📄 Generated LinkedIn Post")
    post_content = st.session_state.get("post", "")
    st.text_area("Post Content:", value=post_content, height=400)
    # Copy to Clipboard button
    if post_content:       

        # Download as text file
        st.download_button(
            label="⬇️ Download Post",
            data=post_content,
            file_name="linkedin_post.txt",
            mime="text/plain"
        )

        # -----------------------
    # Copy button using HTML + JS
    # -----------------------
    import streamlit.components.v1 as components

    copy_html = f"""
    <div style="margin-top:10px;">
        <button style="
            background-color:#4CAF50;
            color:white;
            border:none;
            padding:8px 16px;
            font-size:16px;
            border-radius:5px;
            cursor:pointer;"
            onclick="navigator.clipboard.writeText(`{post_content}`);
                     alert('✅ Post copied to clipboard!');">
            📋 Copy Post
        </button>
    </div>
    
    """
    components.html(copy_html, height=60)