import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# 1️⃣ Load the embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# 2️⃣ Sample Knowledge Base (Expanded)
documents = [
    "RAG stands for Retrieval-Augmented Generation.",
    "RAG improves language model responses by retrieving relevant documents.",
    "FAISS is a tool for fast vector search in large databases.",
    "Transformers are deep learning models that handle sequential data efficiently.",
    "Hugging Face provides pre-trained transformer models.",
    "A retriever fetches relevant information from an external knowledge base.",
    "Retrieval is crucial for keeping LLMs updated with the latest information.",
    "BERT is a transformer model designed for NLP tasks like classification and question answering.",
    "Vector search helps find similar text by comparing embeddings.",
    "Embedding models convert text into numerical vectors for similarity comparisons."
]

# 3️⃣ Convert Documents to Embeddings
doc_embeddings = np.array(embedding_model.encode(documents), dtype=np.float32)

# 4️⃣ Build the FAISS Index
dimension = doc_embeddings.shape[1]  # Get embedding size
index = faiss.IndexFlatL2(dimension)  # L2 Distance-based FAISS index
index.add(doc_embeddings)  # Add document embeddings to the index

# 5️⃣ Define the Retrieval Function
def retrieve_relevant_docs(query, top_k=3):
    """Retrieves the top-k most relevant documents for a given query."""
    query_embedding = np.array(embedding_model.encode([query]), dtype=np.float32)
    distances, indices = index.search(query_embedding, top_k)
    return [(documents[i], distances[0][j]) for j, i in enumerate(indices[0])]

# 6️⃣ Example Queries
if __name__ == "__main__":
    query = "What is retrieval in RAG?"
    results = retrieve_relevant_docs(query)

    print(f"\n🔍 Query: {query}")
    print("💡 Retrieved Documents:")
    for doc, score in results:
        print(f"   - {doc} (Score: {score:.4f})")
