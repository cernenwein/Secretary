FROM python:3.11-slim

WORKDIR /app
COPY tts_speaker.py /app/tts_speaker.py

RUN apt-get update && apt-get install -y ffmpeg curl && \
    pip install numpy soundfile onnxruntime && \
    mkdir -p /app/piper && \
    curl -L -o /app/piper/en_US-amy-medium.onnx https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/en_US-amy-medium.onnx && \
    curl -L -o /app/piper/en_US-amy-medium.onnx.json https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/en_US-amy-medium.onnx.json

VOLUME ["/shared_memory"]

CMD ["python3", "tts_speaker.py"]
