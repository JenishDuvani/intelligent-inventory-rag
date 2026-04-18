from app.embeddings import embed_text

vec = embed_text("inventory demand increased in south region")

print("Vector length:", len(vec))
print(vec[:10])