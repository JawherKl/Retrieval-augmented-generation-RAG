## ⚙️ How RAG Works
RAG combines two key processes:

1. **Retrieval**: 
   - Queries an external knowledge base (e.g., vector database, search index) to fetch relevant documents.
   - Utilizes embeddings and similarity search to find contextually relevant data.

2. **Generation**:
   - Passes the retrieved information to a language model.
   - Generates responses based on both retrieved knowledge and internal model capabilities.

![RAG-phases](assets/RAG-phases.png)

This enables the model to dynamically retrieve up-to-date facts and generate responses grounded in external knowledge.
