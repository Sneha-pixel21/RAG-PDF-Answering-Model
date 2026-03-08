import gradio as gr
import os
from pdf_loader import extract_text_from_pdf
from chunking import chunk_text
from embeddings import generate_embeddings, embed_query
from rag_pipeline import generate_answer
from rag_pipeline import generate_question
from vector_db import add_chunks_to_db, search_documents, get_uploaded_sources

index = None
chunks = None

def process_pdf(pdf_file):
    global chunks
    pages = extract_text_from_pdf(pdf_file.name)
    chunks = chunk_text(pages)
    embeddings = generate_embeddings([c["text"] for c in chunks])
    pdf_file = os.path.basename(pdf_file.name)
    add_chunks_to_db(chunks, embeddings, pdf_file)
    sample_context = " ".join([c["text"]for c in chunks[:5]])
    questions = generate_question(sample_context)
    status_message = f"""
    Stored {len(chunks)} chunks from {pdf_file} into database.

    You can upload another PDF to expand the database.

    Document stored:
    {chr(10).join(get_uploaded_sources())}
    """
    docs = "\n".join(get_uploaded_sources())
    return status_message, questions, docs


def ask_question(question):
    query_embedding = embed_query(question)
    results = search_documents(query_embedding)
    
    retrived_chunks = "\n\n".join(
        [
            f"(Source: {results['metadatas'][0][i]['source']}, Page: {results['metadatas'][0][i]['page']})"
            f"{results['documents'][0][i]}"
            for i in range(len(results['documents'][0]))
        ]
    )
    
    answer = generate_answer(retrived_chunks, question)
    references = "\n".join(
    [
        f"{results['metadatas'][0][i]['source']} (Page: {results['metadatas'][0][i]['page']})"
        for i in range(len(results['documents'][0]))
    ])
    return f"Answer: {answer}\n\nReferences:\n{references}"

exixting_docs= get_uploaded_sources()
if len(exixting_docs) == 0:
    exixting_docs_text = "No documents uploaded yet."
else:
    exixting_docs_text = "Existing documents in database:\n" + "\n".join(exixting_docs)


with gr.Blocks() as demo:
    gr.Markdown("# PDF Question Answering Model:\n Upload a PDF and ask questions about its content.")

    with gr.Row():

        with gr.Column(scale=3):
            pdf_input = gr.File(label="Upload PDF")
            process_button = gr.Button("Process PDF")
            question = gr.Textbox(label="Ask a question about the PDF")
            answer = gr.Textbox(label="Answer:", lines=15)
            upload_new_pdf = gr.Button("Upload another PDF")
           

        with gr.Column(scale=1):
             status = gr.Textbox(label = "Status")
             suggested_questions = gr.Textbox(label= "Suggested Questions", lines=5)
             stored_docs = gr.Textbox(label="Existing Documents in Database", value=exixting_docs_text, lines=5,interactive=False)

    def clear_pdf():
        return None, " "

    upload_new_pdf.click(
        clear_pdf,
        outputs=[pdf_input, status]
    )

    process_button.click(
        process_pdf, 
        inputs=pdf_input, 
        outputs=[status, suggested_questions, stored_docs]
        )
    question.submit(ask_question, inputs=question, outputs=answer)



demo.launch()
