from pdf_reader import read_pdfs
from chunker import chunk_documents
from embeddings import create_embeddings, create_query_embedding
from vector_store import VectorStore
from llm import generate_answer


class ResearchAgent:
    """
    AI Research Agent Backend
    Handles:
    - PDF Loading
    - Chunking
    - Embedding Generation
    - Vector Search
    - Answer Generation
    """

    def __init__(self, data_folder="data"):

        self.data_folder = data_folder
        self.vector_db = None

        self.initialize()

    def initialize(self):

        print("\n📚 Loading PDF documents...")

        documents = read_pdfs(self.data_folder)

        if len(documents) == 0:
            raise Exception("No PDF files found inside the data folder.")

        print(f"✅ Loaded {len(documents)} pages.")

        print("✂ Chunking documents...")

        chunks = chunk_documents(documents)

        print(f"✅ Created {len(chunks)} chunks.")

        print("🧠 Creating embeddings...")

        embeddings = create_embeddings(chunks)

        print("✅ Embeddings created.")

        print("📦 Building FAISS Vector Store...")

        self.vector_db = VectorStore(embeddings.shape[1])

        self.vector_db.add_embeddings(
            embeddings,
            chunks
        )

        print("✅ Research Agent Ready!\n")

    def retrieve(self, question, top_k=5):

        query_embedding = create_query_embedding(question)

        return self.vector_db.search(
            query_embedding,
            top_k
        )

    def ask(self, question):

        retrieved_chunks = self.retrieve(question)
        print(f"🔍 \n===== RETRIEVED CHUNKS =====")
        for i, item in enumerate(retrieved_chunks, start=1):
            print(f"\nChunk {i}")
            print("File:", item["chunk"]["filename"])
            print("Page:", item["chunk"]["page"])
            print("Similarity:", item["similarity"])
            print(item["chunk"]["content"][:500])
        print("=============================\n")    
        

        answer = generate_answer(
            question,
            retrieved_chunks
        )

        evidence = []

        seen = set()

        for item in retrieved_chunks:

            chunk = item["chunk"]

            filename = chunk["filename"]
            page = chunk["page"]
            similarity = round(item["similarity"] * 100, 2)

            key = (filename, page)

            if key not in seen:

                seen.add(key)

                evidence.append({

                    "filename": filename,
                    "page": page,
                    "similarity": similarity,
                    "content": chunk["content"]

                })

        return {

            "answer": answer,
            "evidence": evidence

        }