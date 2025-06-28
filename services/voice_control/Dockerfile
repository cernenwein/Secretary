FROM python:3.11-slim

WORKDIR /app
COPY voice_control.py /app/voice_control.py

RUN pip install faster-whisper

CMD ["python3", "voice_control.py"]
