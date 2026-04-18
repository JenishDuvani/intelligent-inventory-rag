import requests

# Replace with your EC2 public IP
FAISS_API_URL = "http://13.126.152.58:8000"


class FaissClient:
    def __init__(self, base_url=FAISS_API_URL):
        self.base_url = base_url

    def health(self):
        url = f"{self.base_url}/health"
        r = requests.get(url)
        print("Status:", r.status_code)
        print("Response text:", r.text)
        return r.text

    def index_vectors(self, vectors, metadata):
        """
        vectors: list of lists (embeddings)
        metadata: list of metadata objects
        """

        url = f"{self.base_url}/index"

        payload = {
            "vectors": vectors,
            "metadata": metadata
        }

        r = requests.post(url, json=payload)

        print("Status:", r.status_code)
        print("Response text:", r.text)
        return r.text

    def search(self, query_vector, top_k=3):
        """
        query_vector: embedding list
        """

        url = f"{self.base_url}/search"

        payload = {
            "query_vector": query_vector,
            "top_k": top_k
        }

        r = requests.post(url, json=payload)

        print("Status:", r.status_code)
        print("Response text:", r.text)
        return r.json()