import streamlit as st
from transformers import pipeline

# Load the summarization model
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
except Exception as e:
    st.error(f"Model load error: {e}")

st.set_page_config(page_title="AI Text Summarizer")
st.title("🧠 AI Text Summarizer")
st.write("Enter an article or paragraph. The AI will generate a summary.")

user_input = st.text_area("📄 Paste your paragraph here", height=300)

if st.button("Summarize"):
    if user_input.strip() != "":
        with st.spinner("Summarizing..."):
            try:
                summary = summarizer(user_input, max_length=130, min_length=30, do_sample=False)
                st.subheader("📝 Summary:")
                st.success(summary[0]['summary_text'])
            except Exception as e:
                st.error(f"Error during summarization:\n{e}")
    else:
        st.warning("⚠️ Please enter some text to summarize.")
