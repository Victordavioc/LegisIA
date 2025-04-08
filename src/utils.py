# src/utils.py
import os
from PyPDF2 import PdfReader

def load_pdfs_from_folder(folder_path):
    texts = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            path = os.path.join(folder_path, filename)
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            texts.append(text)
    return texts
