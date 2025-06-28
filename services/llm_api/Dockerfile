FROM python:3.11-slim

WORKDIR /app
COPY llm_api.py /app/llm_api.py

RUN pip install flask

EXPOSE 11434
CMD ["python3", "llm_api.py"]
