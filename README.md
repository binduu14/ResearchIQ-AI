# 📚 ResearchIQ AI

An AI-powered Research Assistant that performs semantic search over PDF documents using Retrieval-Augmented Generation (RAG).

Developed for the **Rooman AI Challenge 2026**.

---

## 🚀 Features

- 📄 Read multiple PDF documents
- 🧠 Semantic Search using Sentence Transformers
- 🔍 FAISS Vector Database
- 🤖 Groq Llama 3.3 70B for answer generation
- 📑 Source citations with page numbers
- 💬 Interactive Streamlit interface
- 📚 Evidence display with similarity score

---

## 🏗️ Project Architecture

```
PDF Documents
      │
      ▼
 PDF Reader (PyMuPDF)
      │
      ▼
 Text Chunking
      │
      ▼
 Sentence Transformers
      │
      ▼
 FAISS Vector Database
      │
      ▼
 Relevant Chunks
      │
      ▼
 Groq Llama 3.3 70B
      │
      ▼
 Final Answer + Citations
```

---

## 🛠️ Technologies Used

- Python
- Streamlit
- FAISS
- Sentence Transformers
- PyMuPDF
- Groq API
- NumPy

---

## 📂 Project Structure

```
ResearchAgent/
│
├── app.py
├── streamlit_app.py
├── backend.py
├── pdf_reader.py
├── chunker.py
├── embeddings.py
├── vector_store.py
├── llm.py
├── config.py
├── requirements.txt
├── data/
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ResearchIQ-AI.git
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```
GROQ_API_KEY=your_api_key
```

Run

```bash
python -m streamlit run streamlit_app.py
```

---

## 📄 Sample Questions

- What are the principles of Responsible AI?
- Explain Machine Learning.
- What are common AI applications?
- How does Microsoft define Responsible AI?

---

## 👨‍💻 Developer

**Soyeah B**

BE – Computer Science & Business Systems

K S School of Engineering & Management

Rooman AI Challenge 2026