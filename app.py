import streamlit as st

from ai import ask_ai_safe


# Configure the page
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝"
)

# Application title
st.title("AI Text Summarizer")

# Instructions
st.write(
    "Paste your text below and let AI summarize "
    "the main ideas into three bullet points."
)

# Text input area
text = st.text_area(
    "Paste your text here",
    height=250,
    placeholder="Enter or paste your text..."
)

# Summarize button
if st.button("Summarize"):

    if not text.strip():
        st.warning("Please enter some text first.")

    else:
        prompt = (
            "Summarize the following text in exactly "
            "three concise bullet points. Preserve the "
            "main ideas and do not invent information.\n\n"
            + text
        )

        with st.spinner("AI is summarizing your text..."):

            summary = ask_ai_safe(prompt)

        st.subheader("Your Summary")
        st.write(summary)