import boto3
import json
from retrieval_pipeline import retrieve_context

# bedrock = boto3.client(
#     service_name="bedrock-runtime",
#     region_name="us-east-1"
# )

# # DEFAULT_MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"
# # DEFAULT_MODEL_ID = "us.anthropic.claude-3-5-haiku-20241022-v1:0"
# DEFAULT_MODEL_ID = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"

# def generate_answer(user_query, top_k=3, model_id=DEFAULT_MODEL_ID):

#     retrieval_results = retrieve_context(user_query, top_k=top_k)

#     contexts = []

#     for r in retrieval_results["results"]:
#         metadata = r["metadata"]

#         if "text" in metadata:
#             contexts.append(metadata["text"])
#         else:
#             contexts.append(str(metadata))

#     context_text = "\n".join(contexts)

#     prompt = f"""
# You are an intelligent inventory and demand forecasting assistant.

# Use the retrieved context below to answer the user's question.

# Retrieved Context:
# {context_text}

# User Question:
# {user_query}

# Answer:
# """

#     body = {
#         "anthropic_version": "bedrock-2023-05-31",
#         "max_tokens": 300,
#         "messages": [
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     }

#     response = bedrock.invoke_model(
#         modelId=model_id,
#         body=json.dumps(body)
#     )

#     result = json.loads(response["body"].read())

#     return result["content"][0]["text"]


bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

DEFAULT_MODEL_ID = "us.anthropic.claude-sonnet-4-5-20250929-v1:0"

DEFAULT_SYSTEM_PROMPT = """
You are an intelligent inventory and demand forecasting assistant.

Your job is to:
- Analyze inventory issues
- Explain demand trends
- Suggest supplier actions
- Answer only from the provided retrieved context
- Clearly mention when information is unavailable
"""


def generate_answer(
    user_query,
    top_k=3,
    model_id=DEFAULT_MODEL_ID,
    system_prompt=DEFAULT_SYSTEM_PROMPT
):

    retrieval_results = retrieve_context(user_query, top_k=top_k)

    contexts = []

    for r in retrieval_results["results"]:
        metadata = r["metadata"]

        if "text" in metadata:
            contexts.append(metadata["text"])
        else:
            contexts.append(str(metadata))

    context_text = "\n".join(contexts)

    final_prompt = f"""
{system_prompt}

Retrieved Context:
{context_text}

User Question:
{user_query}

Answer:
"""

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "messages": [
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    }

    response = bedrock.invoke_model(
        modelId=model_id,
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())

    return result["content"][0]["text"]