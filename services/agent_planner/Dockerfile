FROM python:3.11-slim

WORKDIR /app
COPY planner.py /app/planner.py

RUN pip install requests dateparser

VOLUME ["/shared_memory"]

CMD ["python3", "planner.py"]
