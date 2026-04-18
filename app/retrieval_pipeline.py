from embeddings import embed_text
from faiss_client import FaissClient

faiss = FaissClient()


def retrieve_context(query, top_k=3):
    """
    query: user question
    """

    print("Generating query embedding...")

    query_vector = embed_text(query)

    print("Searching FAISS...")

    results = faiss.search(query_vector, top_k=top_k)

    return results