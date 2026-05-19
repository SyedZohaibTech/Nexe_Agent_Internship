import os
import faiss
import numpy as np
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
document_vectors = []


def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def create_vector_store(text):
    global documents
    global document_vectors

    chunks = text.split("\n")
    chunks = [chunk for chunk in chunks if chunk.strip() != ""]
    documents = chunks

    embeddings = embedding_model.encode(chunks)
    document_vectors = np.array(embeddings, dtype=np.float32)

    index = faiss.IndexFlatL2(document_vectors.shape[1])
    index.add(document_vectors)
    return index


def ask_question(index, question):
    question_embedding = embedding_model.encode([question])
    question_embedding = np.array(question_embedding, dtype=np.float32)

    distances, indices = index.search(question_embedding, 3)

    context = ""
    for idx in indices[0]:
        context += documents[idx] + "\n"

    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content