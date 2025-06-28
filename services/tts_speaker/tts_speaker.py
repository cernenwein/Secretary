import os
import time
import json
import numpy as np
import soundfile as sf
import subprocess
import onnxruntime as ort

INPUT_FILE = "/shared_memory/planner_output.txt"
TEMP_WAV = "/app/output.wav"
VOICE_PATH = "/app/piper/en_US-amy-medium.onnx"
CONFIG_PATH = "/app/piper/en_US-amy-medium.onnx.json"

print("🗣️ Piper TTS speaker loading...")

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

sample_rate = config["sample_rate"]
session = ort.InferenceSession(VOICE_PATH)

symbols = {c: i for i, c in enumerate(config["symbols"])}
silence_id = symbols.get("_", 0)

def text_to_ids(text):
    return [symbols.get(c, silence_id) for c in text.lower()]

def synthesize(text):
    input_ids = np.array([text_to_ids(text)], dtype=np.int64)
    ort_inputs = {"input": input_ids}
    ort_outs = session.run(None, ort_inputs)
    audio = ort_outs[0].squeeze().astype(np.float32)
    return audio

def speak(text):
    print(f"📣 Speaking: {text}")
    audio = synthesize(text)
    sf.write(TEMP_WAV, audio, samplerate=sample_rate)
    subprocess.run(["ffplay", "-nodisp", "-autoexit", TEMP_WAV], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

last_spoken = ""

print("🎤 TTS speaker ready. Watching for planner output...")

while True:
    if os.path.exists(INPUT_FILE):
        with open(INPUT_FILE, "r") as f:
            text = f.read().strip()
        if text and text != last_spoken:
            speak(text)
            last_spoken = text
    time.sleep(1)
