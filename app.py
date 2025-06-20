import streamlit as st
from transformers import pipeline

# Set page configuration
st.set_page_config(page_title="🧠 AI Text Summarizer", page_icon="🧠", layout="centered")

# Page title and subtitle with styling
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🧠 AI Text Summarizer</h1>
    <p style='text-align: center; font-size: 18px;'>Paste a paragraph or article below, and get a concise AI-generated summary instantly!</p>
""", unsafe_allow_html=True)

# Load the summarization model
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
except Exception as e:
    st.error("❌ Model load error:")
    st.exception(e)
    st.stop()

# User input box
user_input = st.text_area("📄 Paste your paragraph here:", height=300)

# Summarize button logic
if st.button("🚀 Summarize"):
    if user_input.strip() != "":
        with st.spinner("✨ Summarizing... Please wait..."):
            try:
                summary = summarizer(user_input, max_length=130, min_length=30, do_sample=False)
                st.markdown("### 📝 Summary:")
                st.markdown(
                    f"<div style='background-color:#f0f2f6; padding:15px; border-radius:10px; font-size:16px;'>{summary[0]['summary_text']}</div>",
                    unsafe_allow_html=True
                )
            except Exception as e:
                st.error("❌ Error during summarization:")
                st.exception(e)
    else:
        st.warning("⚠️ Please enter some text to summarize.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 14px;'>Made with ❤️ by Tanishka</p>",
    unsafe_allow_html=True
)
