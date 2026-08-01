def chunk_documents(documents, chunk_size=1000, overlap=200):
    """
    Split each page into overlapping chunks while preserving
    the filename and page number for citations.
    """

    chunks = []

    for doc in documents:

        text = doc["text"]
        filename = doc["filename"]
        page = doc["page"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk = text[start:end]

            if chunk.strip():

                chunks.append({
                    "filename": filename,
                    "page": page,
                    "content": chunk
                })

            start += chunk_size - overlap

    return chunks