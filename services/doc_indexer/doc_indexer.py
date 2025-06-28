import os
import json
from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader

DOC_DIR = "/shared_memory/docs"
OUTPUT_FILE = "/shared_memory/doc_memory.json"
MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    elif file_path.endswith(".txt") or file_path.endswith(".md"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def chunk_text(text, max_length=500):
    chunks, current = [], ""
    for sentence in text.split(". "):
        if len(current) + len(sentence) < max_length:
            current += sentence + ". "
        else:
            chunks.append(current.strip())
            current = sentence + ". "
    if current:
        chunks.append(current.strip())
    return chunks

def index_documents():
    memory = []
    for fname in os.listdir(DOC_DIR):
        fpath = os.path.join(DOC_DIR, fname)
        if not os.path.isfile(fpath):
            continue
        print(f"📄 Indexing: {fname}")
        text = extract_text(fpath)
        for chunk in chunk_text(text):
            embedding = model.encode(chunk).tolist()
            memory.append({
                "filename": fname,
                "text": chunk,
                "embedding": embedding
            })
    with open(OUTPUT_FILE, "w") as f:
        json.dump(memory, f, indent=2)
    print(f"✅ Indexed {len(memory)} chunks to {OUTPUT_FILE}")

index_documents()
