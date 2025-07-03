FROM python:3.11-slim

WORKDIR /app


RUN apt-get update && apt-get install -y ffmpeg curl && \
    pip install numpy soundfile onnxruntime 

COPY piper/en_US-amy-medium.onnx /app/piper/en_US-amy-medium.onnx
COPY piper/en_US-amy-medium.onnx.json /app/piper/en_US-amy-medium.onnx.json
COPY tts_speaker.py /app/tts_speaker.py


    
VOLUME ["/shared_memory"]

CMD ["python3", "tts_speaker.py"]
