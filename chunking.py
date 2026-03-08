def chunk_text(pages, chunk_size=300, overlap=50):
    chunks = []

    for page in pages:
        words = page["text"].split()

        start = 0
        while start < len(words):
            end = start + chunk_size
            chunk_words = words[start:end]

            chunks.append({
                "text": " ".join(chunk_words),
                "page": page["page"]
            })

            start += chunk_size - overlap

    return chunks