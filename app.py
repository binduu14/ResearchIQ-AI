from backend import ResearchAgent

print("=" * 70)
print("📚 AI Research Agent")
print("=" * 70)

agent = ResearchAgent()

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        print("\n👋 Thank you for using the AI Research Agent!")
        break

    result = agent.ask(question)

    print("\n" + "=" * 70)
    print("💡 ANSWER")
    print("=" * 70)

    print(result["answer"])

    print("\n📄 EVIDENCE")
    print("-" * 70)

    for item in result["evidence"]:

        print(f"📘 {item['filename']}")
        print(f"   Page       : {item['page']}")
        print(f"   Similarity : {item['similarity']}%")
        print()