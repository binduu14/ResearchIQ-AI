from vector_store import VectorStore

def test_vector_store_creation():
    vector_db = VectorStore(384)
    assert vector_db is not None

def test_vector_store_add_embeddings():
    vector_db = VectorStore(384)    