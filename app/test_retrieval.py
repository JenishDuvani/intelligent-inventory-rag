from app.retrieval_pipeline import retrieve_context

query = "Which warehouse has inventory shortage?"

results = retrieve_context(query)

print(results)