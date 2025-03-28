import faiss
import numpy as np
from transformers import pipeline
from sentence_transformers import SentenceTransformer

# 1️⃣ Load the embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# 2️⃣ Sample knowledge base
documents = [
    "RAG stands for Retrieval-Augmented Generation.",
    "RAG combines retrieval and generation to improve response accuracy.",
    "Large Language Models (LLMs) like GPT struggle with real-time updates.",
    "Retrievers fetch relevant documents from an external knowledge base.",
    "FAISS is a library for efficient similarity search."
]

# 3️⃣ Convert documents to embeddings
doc_embeddings = np.array(embedding_model.encode(documents), dtype=np.float32)

# 4️⃣ Build FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

# 5️⃣ Define retrieval function
def retrieve_relevant_docs(query, top_k=2):
    query_embedding = np.array(embedding_model.encode([query]), dtype=np.float32)
    distances, indices = index.search(query_embedding, top_k)
    return [documents[i] for i in indices[0]]

# 6️⃣ Load a text generation model (FIXED)
generator = pipeline("text-generation", model="gpt2")

# 7️⃣ Define the RAG pipeline
def simple_rag_pipeline(query):
    retrieved_docs = retrieve_relevant_docs(query)
    context = " ".join(retrieved_docs)
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    response = generator(prompt, max_length=255, num_return_sequences=1)
    return response[0]['generated_text']

# 8️⃣ Test the script
query = "What is RAG?"
response = simple_rag_pipeline(query)

print("\n🔍 Query:", query)
print("💡 Retrieved Documents:", retrieve_relevant_docs(query))
print("📝 Generated Response:", response)
