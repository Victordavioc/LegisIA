from qa_chain import build_qa_chain

def main():
    qa = build_qa_chain()
    print("⚖️  LegisIA - Assistente Jurídico Inteligente")
    print("Digite sua pergunta sobre leis brasileiras (ou 'sair')\n")

    while True:
        query = input("Você: ")
        if query.lower() in ["sair", "exit", "quit"]:
            break

        result = qa.invoke({"query": query})
        print("\nResposta:\n", result["result"], "\n")

if __name__ == "__main__":
    main()
