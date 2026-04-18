from typing import List, Dict

def block_chunking(
    text: str,
    chunk_size: int,
    overlap: int,
    metadata: Dict
) -> List[Dict]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append({
            "content": text[start:end],
            "metadata": metadata
        })
        start += chunk_size - overlap

    return chunks


def page_chunking(
    text: str,
    page_delimiter: str,
    metadata: Dict,
    fallback_page_size: int = 1200
) -> List[Dict]:
    """
    Page-based chunking with fallback if delimiter is missing.
    """

    # Case 1: Real page delimiter exists
    if page_delimiter in text:
        pages = text.split(page_delimiter)
    else:
        # Case 2: Fallback - create virtual pages
        pages = [
            text[i:i + fallback_page_size]
            for i in range(0, len(text), fallback_page_size)
        ]

    chunks = []
    for i, page in enumerate(pages):
        if page.strip():
            chunks.append({
                "content": page.strip(),
                "metadata": {
                    **metadata,
                    "page_number": i + 1
                }
            })

    return chunks

