import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
    INDEX_NAME = "compliance-checker"
    EMBEDDING_DIM = 768
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 100
