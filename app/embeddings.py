# app/embeddings.py

import boto3
import json

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

MODEL_ID = "amazon.titan-embed-text-v2:0"


def embed_text(text: str):
    """
    Generate embedding vector for a single text
    """

    body = json.dumps({
        "inputText": text
    })

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=body
    )

    result = json.loads(response["body"].read())

    return result["embedding"]


def embed_batch(texts):
    """
    Generate embeddings for multiple texts
    """

    vectors = []

    for i, t in enumerate(texts):
        print(f"Embedding chunk {i + 1}/{len(texts)}")
        vectors.append(embed_text(t))

    return vectors