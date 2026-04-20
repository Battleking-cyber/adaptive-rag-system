# Adaptive RAG Inference System

## 📌 Objective

The goal of this project is to build an adaptive Retrieval-Augmented Generation (RAG) system that dynamically optimizes retrieval and response generation at inference time.

---

## 🧠 Architecture Diagram

```
User Query
   ↓
Adaptive Decision Layer
   ↓
Hybrid Retriever (FAISS + BM25)
   ↓
Re-ranking (basic merging)
   ↓
Generator
   ↓
Response + Feedback Loop
```

---

## ⚙️ System Components

### 1. Document Ingestion

* Supports TXT and PDF files
* Extracts and preprocesses text

### 2. Vector Index (FAISS)

* Converts documents into embeddings
* Enables fast semantic search

### 3. Hybrid Retrieval

* Combines:

  * Vector search (semantic similarity)
  * Keyword search (BM25)
* Improves retrieval accuracy

### 4. Adaptive Decision Layer

* Dynamically adjusts Top-K based on query complexity
* Short queries → smaller K
* Long queries → larger K

### 5. Feedback Loop

* Tracks:

  * Retrieval time
  * Generation time
* Helps optimize system performance

---

## 📊 Performance Measurement

* Retrieval Time
* Generation Time
* Total Latency
* Adaptive behavior impact

---

## ⚖️ Design Decisions

* Used FAISS for efficient similarity search
* Hybrid retrieval to balance semantic and keyword matching
* Rule-based adaptive logic for simplicity and clarity
* Lightweight generator for fast response time

---

## ⚠️ Trade-offs

* Simple generator instead of advanced LLM (less intelligent output)
* Rule-based adaptation instead of learned optimization
* No deep re-ranking model (basic merging used)

---

## 🚀 How to Run

```
pip install -r requirements.txt
cd src
python main.py
```

---

## 📌 Example Query

```
Ask: What is Mass Layoff Statistics?
```

---

## 🔥 Future Improvements

* Integrate LLM (GPT / HuggingFace)
* Add UI (Streamlit)
* Improve re-ranking with ML models
* Add caching layer
* Implement query decomposition

---
