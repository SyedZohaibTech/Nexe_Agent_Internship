import streamlit as st
from rag import (
    load_pdf,
    create_vector_store,
    ask_question
)

import os

st.set_page_config(
    page_title="RAG Assistant",
    page_icon="📚"
)

st.title("📚 RAG Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    os.makedirs(
        "uploaded_docs",
        exist_ok=True
    )

    file_path = os.path.join(
        "uploaded_docs",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF Uploaded ✅")

    text = load_pdf(file_path)

    index = create_vector_store(text)

    question = st.text_input(
        "Ask Question"
    )

    if st.button("Get Answer"):

        answer = ask_question(
            index,
            question
        )

        st.subheader("🤖 Answer")

        st.write(answer)