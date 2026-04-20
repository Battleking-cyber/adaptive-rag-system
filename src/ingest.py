import os
from PyPDF2 import PdfReader

def load_documents(folder_path):
    docs = []

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                docs.extend(f.readlines())

        elif file.endswith(".pdf"):
            reader = PdfReader(path)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    docs.append(text)

    docs = [doc.strip() for doc in docs if doc]
    return docs
