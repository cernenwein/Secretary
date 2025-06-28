from flask import Flask, request, jsonify
import os

app = Flask(__name__)

MODEL_PATH = "/models/mistral-7b-instruct.Q4_K_M.gguf"

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json.get("prompt", "")
    print(f"🧠 LLM received prompt: {prompt[:100]}...")
    # Simulate response for now
    return jsonify({"response": f"I heard: {prompt}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=11434)
