import faiss # type: ignore
import numpy as np # type: ignore


class VectorStore:
    def __init__(self, dimension):
        """
        Initialize a FAISS index using Cosine Similarity.
        """

        self.index = faiss.IndexFlatIP(dimension)
        self.chunks = []

    def add_embeddings(self, embeddings, chunks):
        """
        Store embeddings in FAISS.
        """

        embeddings = np.array(embeddings).astype("float32")

        # Normalize vectors for cosine similarity
        faiss.normalize_L2(embeddings)

        self.index.add(embeddings)

        self.chunks = chunks

    def search(self, query_embedding, top_k=5):
        """
        Retrieve the most similar chunks.
        """

        query_embedding = np.array([query_embedding]).astype("float32")

        faiss.normalize_L2(query_embedding)

        similarities, indices = self.index.search(query_embedding, top_k)

        results = []

        for similarity, index in zip(similarities[0], indices[0]):

            if index == -1:
                continue

            results.append({
                "similarity": float(similarity),
                "chunk": self.chunks[index]
            })

        return results