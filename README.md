# AI-Powered PDF Question Answering System (RAG)

An end-to-end **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and interactively ask questions about their content.
The system processes documents, stores semantic embeddings in a **ChromaDB vector database**, retrieves relevant information using similarity search, and generates context-aware answers using a **local Large Language Model (LLM) via Ollama**.

The application includes a **Gradio-based web interface** for uploading documents, managing stored PDFs, generating suggested questions, and querying the knowledge base with source references.

---

# Overview

Large Language Models are powerful but often lack access to external or private knowledge.
This project solves that problem using **Retrieval-Augmented Generation (RAG)**.

Instead of relying only on model training data, the system:

1. Converts documents into **vector embeddings**
2. Stores them in a **vector database**
3. Retrieves the most relevant content when a user asks a question
4. Provides this context to an LLM to generate accurate responses

This enables **AI-powered document understanding and search**.

---

# Key Features

### Multi-PDF Knowledge Base

* Upload and process multiple PDF documents
* Expand the knowledge base over time
* Store documents persistently in a vector database

### Semantic Document Understanding

* Text extraction from PDFs
* Smart text chunking
* Embedding generation using **Sentence Transformers**

### Intelligent Retrieval

* Vector similarity search using **ChromaDB**
* Finds the most relevant sections of documents
* Improves answer accuracy using contextual retrieval

### AI Answer Generation

* Local LLM inference using **Ollama**
* Context-aware responses generated using retrieved document chunks

### Source References

* Each answer includes **page references**
* Allows users to verify information directly in the original document

### Interactive Web Interface

Built with **Gradio**, enabling users to:

* Upload PDFs
* View stored documents
* Generate suggested questions
* Ask questions about documents
* Receive AI-generated answers with references

---

# System Architecture

The system follows a **Retrieval-Augmented Generation (RAG) pipeline**:

```
PDF Upload
     │
     ▼
Text Extraction
     │
     ▼
Text Chunking
     │
     ▼
Embedding Generation
     │
     ▼
Vector Storage
(ChromaDB)
     │
     ▼
User Question
     │
     ▼
Query Embedding
     │
     ▼
Similarity Search
     │
     ▼
Relevant Chunks Retrieved
     │
     ▼
Context + Question → LLM (Ollama)
     │
     ▼
Generated Answer + Page References
```

---

# Project Structure

```
RAG-Project/
│
├── app.py
│   Gradio interface and application entry point
│
├── pdf_loader.py
│   Extracts text from uploaded PDF documents
│
├── chunking.py
│   Splits document text into manageable chunks
│
├── embeddings.py
│   Generates semantic embeddings for document chunks
│
├── vector_db.py
│   Handles ChromaDB storage and similarity search
│
├── rag_pipeline.py
│   Generates answers using retrieved document context
│
├── requirements.txt
│   Project dependencies
│
└── .gitignore
```

---

# Technologies Used

| Technology                | Purpose                        |
| ------------------------- | ------------------------------ |
| **Python**                | Core programming language      |
| **Gradio**                | Web interface                  |
| **ChromaDB**              | Vector database for embeddings |
| **Sentence Transformers** | Embedding generation           |
| **Ollama**                | Local LLM inference            |
| **PyPDF**                 | PDF text extraction            |
| **NumPy**                 | Numerical operations           |

---

#  How the System Works

### 1. Document Processing

When a PDF is uploaded:

* Text is extracted using `PyPDF`
* The document is split into smaller semantic chunks
* Each chunk is converted into vector embeddings

### 2. Vector Database Storage

The embeddings are stored in **ChromaDB** along with metadata:

* Page number
* Source document name

This allows efficient semantic search.

### 3. Question Answering

When a user asks a question:

1. The question is converted into an embedding
2. ChromaDB retrieves the most relevant document chunks
3. These chunks are provided to the LLM as context
4. The LLM generates an answer grounded in the document

### 4. Reference Tracking

The system returns:

* The generated answer
* The source **PDF name**
* The **page numbers** where the information was found

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Sneha-pixel21/RAG-PDF-Answering-Model.git
cd RAG-PDF-Answering-Model
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Install Ollama

Download and install:

https://ollama.com

Pull the model used in the project:

```bash
ollama pull phi3:mini
```

---

## 4. Run the Application

```bash
python app.py
```

Then open:

```
http://127.0.0.1:7860
```

---

# Example Workflow

1️⃣ Upload a PDF document
2️⃣ Click **Process PDF**
3️⃣ View suggested questions
4️⃣ Ask questions about the document
5️⃣ Receive AI-generated answers with page references

---

# Example Use Cases

* Research paper exploration
* AI-powered document search
* Knowledge base assistants
* Enterprise document intelligence
* AI assistants for reports and manuals

---

# Future Improvements

* Chat-style conversation with documents
* Document summarization
* Multi-user support
* Cloud deployment
* Faster retrieval using hybrid search
* Support for additional file formats

---

# License

This project is open-source and available under the **MIT License**.

---

# Author

**Sneha Kushwaha**

AI / Machine Learning Enthusiast
Focused on building intelligent systems using **LLMs, vector databases, and retrieval pipelines**.

---
