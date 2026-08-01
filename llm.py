from groq import Groq # type: ignore
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def generate_answer(question, retrieved_chunks):

    context = ""

    for item in retrieved_chunks:

        chunk = item["chunk"]

        context += f"""
Document: {chunk['filename']}
Page: {chunk['page']}

{chunk['content']}

------------------------------------------
"""

    prompt = f"""
You are a helpful AI Research Assistant.

Use ONLY the information provided in the context below.

Rules:
- Answer only from the context.
- Never invent information.
- If the answer is not present, reply exactly:
"I could not find the answer in the provided source documents."

Context:
{context}

Question:
{question}

Answer:
"""

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You answer questions only using the supplied document context."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            max_tokens=500
        )

        answer = response.choices[0].message.content

        if answer is None:
            return "No answer returned from the language model."

        return answer.strip()

    except Exception as e:

        return f"Error while generating answer: {str(e)}"