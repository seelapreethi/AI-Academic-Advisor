import os
import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./data/chroma_db")
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "all-MiniLM-L6-v2")


# Load embedding model
model = SentenceTransformer(EMBEDDING_MODEL_NAME)


# Create persistent chroma client
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)


# Create collection
collection = client.get_or_create_collection(
    name="conversation_memory"
)


def store_embedding(text: str, turn_id: int):

    embedding = model.encode(text).tolist()

    collection.add(
        embeddings=[embedding],
        documents=[text],
        metadatas=[{"turn_id": turn_id}],
        ids=[str(turn_id)]
    )

    print("Embedding stored successfully")


def search_similar(text: str, k: int = 3):

    embedding = model.encode(text).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=k
    )

    return results