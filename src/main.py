import time
from ingest import load_documents
from embed import create_index
from retrieve import bm25_index, retrieve
from adaptive import dynamic_k
from generate import generate_answer

docs = load_documents("../data")

index, _ = create_index(docs)
bm25 = bm25_index(docs)

while True:
    query = input("Ask: ")

    start = time.time()

    k = dynamic_k(query)
    retrieved_docs = retrieve(query, docs, index, bm25, k)

    mid = time.time()

    answer = generate_answer(query, retrieved_docs)

    end = time.time()

    print("\nAnswer:", answer)
    print(f"Retrieval Time: {mid - start:.2f}s")
    print(f"Generation Time: {end - mid:.2f}s")
    print(f"Total Time: {end - start:.2f}s\n")
