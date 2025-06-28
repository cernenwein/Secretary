FROM python:3.11-slim

WORKDIR /app
COPY doc_indexer.py /app/doc_indexer.py

RUN apt-get update && apt-get install -y poppler-utils && \
    pip install nltk sentence-transformers PyPDF2

VOLUME ["/shared_memory/docs"]

CMD ["python3", "doc_indexer.py"]
