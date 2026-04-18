# app/test_ingestion.py

from app.ingestion_pipeline import index_chunks

chunks = [
    {
        "content": "Demand for rice increased by 30 percent in south India during Q4.",
        "metadata": {
            "text": "Demand for rice increased by 30 percent in south India during Q4.",
            "product": "rice",
            "region": "south",
            "quarter": "Q4"
        }
    },
    {
        "content": "Warehouse 4 is facing inventory shortages for edible oil.",
        "metadata": {
            "text": "Warehouse 4 is facing inventory shortages for edible oil.",
            "warehouse": "4",
            "product": "edible oil"
        }
    }
]

result = index_chunks(chunks)

print(result)