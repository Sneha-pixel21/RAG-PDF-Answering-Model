import requests

def generate_question(context):

    prompt = f"""
You are a helpful AI assistant helping user to explore a document.
use the context below to generate a question that a user might ask about the document.
Context:
{context}

return only the questions as a list.

"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": prompt,
            "stream": False
        }    )
    return response.json()["response"]

    

def generate_answer(context, question):
    prompt = f"""
You are a helpful AI assistant.

use the context below to answer the questoin clearly and in simple terms. 
Context:
{context}

Question:
{question}

Answer:
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]