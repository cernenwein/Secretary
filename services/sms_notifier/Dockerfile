FROM python:3.11-slim

WORKDIR /app
COPY sms_notifier.py /app/sms_notifier.py

RUN pip install twilio

VOLUME ["/shared_memory"]

CMD ["python3", "sms_notifier.py"]
