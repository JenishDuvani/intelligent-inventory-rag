# app/ingestion_pipeline.py

from embeddings import embed_batch
from faiss_client import FaissClient

faiss = FaissClient()


def index_chunks(chunks):
    """
    chunks = [
        {"content": "...", "metadata": {...}}
    ]
    """

    texts = [c["content"] for c in chunks]
    metadata = [c["metadata"] for c in chunks]

    print(f"Generating embeddings for {len(texts)} chunks...")

    vectors = embed_batch(texts)

    print("Sending vectors to FAISS...")

    result = faiss.index_vectors(vectors, metadata)

    return result