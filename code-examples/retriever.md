# 📚 Retriever Module

This module focuses on the **retrieval** component of Retrieval-Augmented Generation (RAG). It efficiently fetches the most relevant documents from a knowledge base using **FAISS** and **Sentence Transformers**.

---

## 🚀 Overview
This script:
✅ Converts text documents into **vector embeddings** using `all-MiniLM-L6-v2`.
✅ Uses **FAISS** (Facebook AI Similarity Search) for fast **vector retrieval**.
✅ Searches the knowledge base to find the **top-K most relevant** documents for a given query.
✅ Returns relevant documents **without** running text generation.

---

## 📂 Repository Structure
```
code-examples/
│── retriever.py   # Core retrieval script
│── simple_rag.py  # Basic RAG implementation (retrieval + generation)
```

---

## 🛠 Installation
Ensure you have Python installed (>=3.8). Then, install dependencies:
```bash
pip install faiss-cpu sentence-transformers numpy
```
👉 If using **GPU**, install FAISS with:
```bash
pip install faiss-gpu
```

---

## 🏃 Running the Script
Run `retriever.py` with:
```bash
python code-examples/retriever.py
```

Example Output:
```
🔍 Query: What is retrieval in RAG?
💡 Retrieved Documents:
   - A retriever fetches relevant information from an external knowledge base. (Score: 0.0000)
   - Retrieval is crucial for keeping LLMs updated with the latest information. (Score: 1.2345)
   - RAG improves language model responses by retrieving relevant documents. (Score: 2.3456)
```

---

## 🔄 How It Works
1️⃣ **Embeds Documents** → Converts text into numerical vectors using `all-MiniLM-L6-v2`.
2️⃣ **Stores Vectors in FAISS** → Enables fast similarity search.
3️⃣ **Retrieves Top-K Relevant Documents** → Based on semantic similarity to the query.

---

## 🚀 Next Steps
✅ Try different queries like **"What is FAISS?"**
✅ Increase the number of documents for better retrieval.
✅ Store documents in a **vector database like Pinecone or ChromaDB** for scalability.

---
