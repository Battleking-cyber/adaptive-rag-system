def generate_answer(query, docs):
    context = " ".join(docs)
    return f"Answer based on context: {context}"
