import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Model Name
MODEL_NAME = "llama-3.3-70b-versatile"

# Embedding Model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Chunk Settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Number of chunks to retrieve
TOP_K = 3