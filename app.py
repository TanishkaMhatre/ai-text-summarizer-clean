import streamlit as st
from transformers import pipeline 

# Load summarization model
summarizer = pipeline("summarization", model='sshleifer/distilbart-cnn-12-6')

# App layout
st.set_page_config(page_title="AI Text Summarizer")
st.title("🧠 AI Text Summarizer")
st.write("Enter an article or paragraph. The AI will generate a summary.")

# User input
user_input = st.text_area("📄 Paste your paragraph here", height=300)

# Summarize button
if st.button("Summarize"):
    if user_input.strip() != "":
        with st.spinner("Summarizing..."):
            summary = summarizer(user_input, max_length=130, min_length=30, do_sample=False)
            st.subheader("📝 Summary:")
            st.success(summary[0]['summary_text'])
    else:
        st.warning("⚠️ Please enter some text to summarize.")
