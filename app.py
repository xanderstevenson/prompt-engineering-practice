from flask import Flask, request, render_template, jsonify
import requests
import os

app = Flask(__name__)

# Load Mistral API key from environment variable
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
AGENT_ID = "ag:a0d6f108:20250813:prompt-crafting-agent:3f92f654"
MISTRAL_API_URL = "https://api.mistral.ai/v1/agents/completions"

def ask_agent(message):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "agent_id": AGENT_ID,
        "messages": [{"role": "user", "content": message}],
        "max_tokens": 500
    }

    try:
        response = requests.post(MISTRAL_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        # Agent reply
        agent_reply = result["choices"][0]["message"]["content"]
        # Convert bold markup to HTML
        agent_reply = agent_reply.replace("**", "<b>").replace("**", "</b>")
        return agent_reply
    except (requests.exceptions.RequestException, KeyError, IndexError) as e:
        print(f"Request error: {e}")
        return "No response from agent"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/init", methods=["GET"])
def init_chat():
    # Send an initial "hi" message to start the conversation
    agent_reply = ask_agent("hi")
    return jsonify({"reply": agent_reply})

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    agent_reply = ask_agent(user_message)
    return jsonify({"reply": agent_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
