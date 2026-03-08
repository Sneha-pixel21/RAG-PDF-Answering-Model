import chromadb
from chromadb.config import Settings 

client = chromadb.Client(
    Settings(
        persist_directory= "chroma_db",
        is_persistent=True
    )
)


collection = client.get_or_create_collection(
    name = "pdf_documents"
)

def add_chunks_to_db(chunks, embeddings, pdf_name):

    ids = []
    documents = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(f"{pdf_name}_{i}")
        documents.append(chunk["text"])
        metadatas.append({
            "page": chunk["page"],
            "source": pdf_name
        })

    collection.add(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,    
        ids=ids
    )


def get_uploaded_sources():
    data = collection.get()

    if not data["metadatas"]:
        return []

    sources = list(set([m["source"] for m in data["metadatas"]]))
    return sources

def search_documents(query_embeddings):
    results = collection.query(
        query_embeddings=query_embeddings,
        n_results=3
    )

    return results
