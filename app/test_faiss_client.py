from app.faiss_client import FaissClient

client = FaissClient()

print("Health check:")
print(client.health())

# dummy_vector = [0.1, 0.2, 0.3, 0.4]
dummy_vector = [0.1] * 1024

print("Indexing vector...")
print(client.index_vectors([dummy_vector], [{"source": "local-test"}]))

print("Searching vector...")
print(client.search(dummy_vector, top_k=1))