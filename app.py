from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 🔗 Replace with your Hugging Face Space URL
HF_SPACE_URL = "https://huggingface.co/spaces/manisha2845/my-text2image-diffuser"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    payload = {"data": [prompt]}
    try:
        resp = requests.post(HF_SPACE_URL, json=payload, timeout=90)
        result = resp.json()
        image_url = result["data"][0]
        return jsonify({"image_url": image_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
