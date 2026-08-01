from sentence_transformers import SentenceTransformer # type: ignore

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    """
    Create normalized embeddings for all document chunks.
    """
    texts = [chunk["content"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings


def create_query_embedding(question):
    """
    Create a normalized embedding for the user's query.
    """
    embedding = model.encode(
        question,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embedding