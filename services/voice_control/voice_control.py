import os
import time

SHARED_FILE = "/shared_memory/voice_input.txt"

print("🎤 Voice control placeholder ready.")

while True:
    # Simulate voice detection
    with open(SHARED_FILE, "w") as f:
        f.write("Simulated voice command at " + time.ctime())
    time.sleep(10)
