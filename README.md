# Intelligent Inventory & Demand Forecast Assistant (RAG-based)

## 📌 Project Description

This project implements a **Retrieval-Augmented Generation (RAG)** based
decision-support system for inventory and demand analysis.

The system allows users to upload business documents, define custom metadata,
apply configurable chunking strategies, and retrieve context-aware insights
using Large Language Models (LLMs) hosted on **AWS Bedrock**.

To ensure performance and scalability, **FAISS vector indexing is hosted on an
AWS EC2 instance**, while the UI and orchestration logic run locally.

This design is:
- Free-tier friendly
- Research-oriented
- Modular and production-aligned

---

## 🎯 Key Objectives

- Convert raw business documents into searchable knowledge
- Support metadata-aware retrieval
- Enable multiple chunking strategies
- Reduce LLM hallucinations using RAG
- Compare different LLM behaviors using the same retrieved context

---

## 🧠 System Architecture

### High-Level Flow

**Local System**
- Upload Document  
- Metadata Input  
- Chunking  
- Send chunks to EC2 via API  

**EC2 Instance**
- Embedding Generation  
- FAISS Vector Index  
- Similarity Search  
- Return top-k relevant chunks  

**Local System**
- LLM (AWS Bedrock)  
- Context-grounded chat response  

---

## 🔌 How Local System Communicates with EC2 (API Design)

The local application and EC2 instance communicate using a lightweight **REST API**
(Flask/FastAPI) exposed by the EC2 instance.

### Responsibilities

**Local System**
- Handles UI (Streamlit)
- Performs document parsing & chunking
- Sends chunks and metadata to EC2
- Sends search queries to EC2
- Receives retrieved context

**EC2 (FAISS Service)**
- Generates embeddings
- Builds & updates FAISS index
- Stores vectors + metadata
- Performs similarity search

### Example API Endpoints

```
POST /index
  → Input: chunks + metadata
  → Action: embed + store in FAISS

POST /search
  → Input: user query
  → Action: similarity search
  → Output: top-k relevant chunks
```

### Data Flow (Simplified)

```
User Query
→ Local App
→ EC2 /search API
→ FAISS Similarity Search
→ Relevant Chunks
→ Local App
→ LLM (AWS Bedrock)
→ Final Answer
```

This separation mirrors real-world production RAG systems and allows
horizontal scaling of the vector store independently from the UI.

---

## 🧱 Technology Stack

### Core
- Python 3.10
- Streamlit
- FAISS
- AWS EC2
- AWS Bedrock

### Libraries
- boto3
- langchain
- langchain-community
- faiss-cpu
- pandas
- numpy
- python-dotenv

---

## 📂 Project Structure

```
intelligent-inventory-rag/
│
├── app/
│   ├── streamlit_app.py     # UI & orchestration
│   ├── chunker.py           # Block & page chunking
│   ├── utils.py             # File readers
│   ├── embeddings.py        # Bedrock embeddings
│   ├── faiss_store.py       # FAISS utilities
│   └── build_index.py       # Chunk → Embed → Index
│
├── api/
│   └── faiss_service.py     # EC2 REST API
│
├── data/
│   └── sample_data.csv
│
├── docs/
│   ├── architecture.md
│   └── prompt_template.md
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## ✅ Current Features

- File upload (CSV, TXT)
- Custom metadata support
- Multiple chunking strategies
- Chunk preview UI
- Session-safe multi-step workflow
- FAISS-compatible document schema

---

## 🚧 Features in Progress

- AWS Bedrock embeddings (Titan)
- EC2-hosted FAISS API
- Similarity-based retrieval
- Chat UI
- Model comparison (Titan vs Claude)

---

## 🛠️ Local Setup

### Prerequisites
- Python 3.10.x
- Git
- AWS account

### Environment Setup

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate    # Windows

pip install --upgrade pip
pip install -r requirements.txt
```

### ▶ Run Locally

```bash
streamlit run app/streamlit_app.py
```

---

## ☁️ EC2 Setup (FAISS Service)

### Instance Configuration
- AMI: Amazon Linux 2023
- Instance Type: t2.micro / t3.micro
- Storage: 16–20 GB

### Python Setup on EC2

```bash
sudo dnf install python3.10 -y
python3.10 -m venv venv
source venv/bin/activate
pip install faiss-cpu fastapi uvicorn numpy pandas
```

> FAISS runs **only on EC2**, not locally.

---

## 🔍 FAISS Strategy

- Vector storage & indexing on EC2
- Index persisted to disk
- Metadata stored alongside vectors
- Local app queries EC2 for retrieval

This avoids local memory limits and reflects production-grade RAG design.

---

## 🔬 Research Scope

- Chunk size vs retrieval quality
- Metadata-aware retrieval
- RAG vs non-RAG outputs
- Hallucination reduction
- Business explainability

---

## 🚀 Future Enhancements

- OpenSearch vector backend
- Hybrid retrieval (BM25 + vectors)
- Authentication & multi-user support
- Evaluation & metrics dashboard

---

## 📌 Academic / Review Notes

This project is designed to be:
- Reproducible
- Modular
- Research-oriented
- Production-aligned

Suitable for **final-year projects, internships, research demos, and RAG experiments**.
