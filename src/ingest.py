import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from utils import load_pdfs_from_folder

load_dotenv()

def ingest_documents(data_path="data/leis"):
    
    texts = load_pdfs_from_folder(data_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )
    docs = splitter.create_documents(texts)

    embeddings = OpenAIEmbeddings(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("vectorstore")

    print("✅ Vetorstore criado e salvo com sucesso!")

if __name__ == "__main__":
    ingest_documents()
