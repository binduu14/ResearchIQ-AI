import os
import streamlit as st # type: ignore
from backend import ResearchAgent

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="ResearchIQ AI",
    page_icon="📚",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main{
    background:#f5f7fb;
}

.block-container{
    padding-top:2rem;
}

.big-title{
    font-size:42px;
    font-weight:700;
    color:#1e3a8a;
}

.subtitle{
    font-size:18px;
    color:#4b5563;
    margin-bottom:20px;
}

.answer-box{
    background:white;
    border-radius:15px;
    padding:20px;
    border-left:6px solid #2563eb;
    box-shadow:0px 2px 12px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# LOAD AGENT
# ==========================================================

@st.cache_resource
def load_agent():
    return ResearchAgent()

agent = load_agent()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=70)

    st.title("ResearchIQ AI")

    st.caption("Semantic Search + Citations")

    st.divider()

    st.subheader("Project")

    st.success("Rooman AI Challenge")

    st.metric("Model","Llama 3.3 70B")

    st.metric("Embeddings","MiniLM-L6-v2")

    st.metric("Vector DB","FAISS")

    pdf_files = [
        f for f in os.listdir("data")
        if f.endswith(".pdf")
    ]

    st.metric("PDF Files",len(pdf_files))

    st.metric("Status","🟢 Ready")

    st.divider()

    st.subheader("Developer")

    
    
    st.success("👨‍💻 Soyeah B")
    st.caption("BE - Computer Science & Business Systems")

    st.caption("K S School of Engineering & Management")

    st.divider()



# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<div style="
background: linear-gradient(135deg,#2563EB,#4F46E5);
padding:35px;
border-radius:20px;
color:white;
">

<h1 style="margin:0;">
📚 ResearchIQ AI
</h1>

<h3>
Semantic Research Assistant
</h3>

<p style="font-size:18px;">
Search across multiple PDF documents using
<b>Semantic Search</b>,
<b>FAISS Vector Database</b>,
<b>Sentence Transformers</b>,
and
<b>Groq Llama 3.3 70B</b>.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# DOCUMENTS
# ==========================================================

st.subheader("📂 Loaded Documents")

cols = st.columns(3)

for i, pdf in enumerate(pdf_files):

    with cols[i % 3]:

     st.markdown(f"""
<div style="
background:white;
padding:15px;
border-radius:12px;
box-shadow:0 3px 10px rgba(0,0,0,0.08);
margin-bottom:15px;
">

📘 <b>{pdf}</b>

</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================================
# QUESTION
# ==========================================================

st.subheader("💬 Ask a Research Question")

question = st.text_area(

    "",

    placeholder="Example: What are the principles of Responsible AI?",

    height=130

)

generate = st.button(

    "🚀 Generate Answer",

    use_container_width=True

)
# ==========================================================
# GENERATE ANSWER
# ==========================================================

if generate:

    if question.strip() == "":

        st.warning("⚠ Please enter a question.")

    else:

        with st.spinner("🔎 Searching documents and generating answer..."):

            try:

                result = agent.ask(question)

                answer = result.get("answer", "").strip()

                evidence = result.get("evidence", [])

            except Exception as e:

                st.error(f"Error: {e}")

                st.stop()

        st.divider()

        # =====================================================
        # ANSWER
        # =====================================================

        st.subheader("💡 AI Answer")

        if answer:

            st.markdown(
                f"""
<div class="answer-box">

{answer}

</div>
""",
                unsafe_allow_html=True,
            )

        else:

            st.warning(
                "The language model did not return an answer."
            )

        st.divider()

        # =====================================================
        # EVIDENCE
        # =====================================================

        st.subheader("📄 Supporting Evidence")

        if len(evidence) == 0:

            st.info("No supporting evidence found.")

        else:

            for item in evidence:

                with st.expander(
                    f"📘 {item['filename']}  |  Page {item['page']}"
                ):

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "Page",
                            item["page"]
                        )

                    with col2:

                        st.metric(
                            "Similarity",
                            f"{item['similarity']}%"
                        )

                    if "content" in item:

                        st.markdown("#### Relevant Passage")

                        st.write(item["content"])
# ==========================================================
# EXAMPLE QUESTIONS
# ==========================================================

st.divider()

st.subheader("💡 Try These Questions")

col1, col2 = st.columns(2)

with col1:

    st.info("• What are the principles of Responsible AI?")

    st.info("• Explain Machine Learning.")

with col2:

    st.info("• What are common AI applications?")

    st.info("• How does Microsoft define Responsible AI?")

# ==========================================================
# PROJECT SUMMARY
# ==========================================================

st.divider()

st.subheader("📊 Project Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 PDF Files", len(pdf_files))

with col2:
    st.metric("🔍 Search Engine", "FAISS")

with col3:
    st.metric("🤖 LLM", "Groq")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
"""
---
### 👨‍💻 Developer

**Soyeah B**

**ResearchIQ AI**  
AI-powered Research Assistant using:

- 📚 Semantic Search
- 🔍 FAISS Vector Database
- 🧠 Sentence Transformers
- 🤖 Groq Llama 3.3 70B
- 🎯 Retrieval-Augmented Generation (RAG)

Built for the **Rooman AI Challenge 2026**
"""
)