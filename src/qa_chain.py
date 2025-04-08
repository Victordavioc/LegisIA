import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI  
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

load_dotenv()

def build_qa_chain():
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
Você é um assistente jurídico inteligente. Use apenas o contexto abaixo, que foi retirado de documentos legais, para responder de forma objetiva à pergunta do usuário.

Contexto:
{context}

Pergunta:
{question}

Resposta:
"""
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt_template},
        return_source_documents=True
    )

    return qa_chain
