FROM python:3.11-slim

WORKDIR /app
COPY web_ui.py /app/web_ui.py

RUN pip install flask

CMD ["python3", "web_ui.py"]
