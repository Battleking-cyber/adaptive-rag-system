from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def bm25_index(docs):
    tokenized = [doc.split() for doc in docs]
    return BM25Okapi(tokenized)

def retrieve(query, docs, index, bm25, k=3):
    query_vec = model.encode([query])

    D, I = index.search(np.array(query_vec), k)
    vector_results = [docs[i] for i in I[0]]

    bm25_scores = bm25.get_scores(query.split())
    keyword_results = [docs[i] for i in np.argsort(bm25_scores)[-k:]]

    results = list(set(vector_results + keyword_results))
    return results
