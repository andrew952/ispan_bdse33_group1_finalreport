import openai
from flask_cors import CORS

# print(response.json())
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder="static")
CORS(app)

# 用您的OpenAI API密钥替换此处字符串
openai.api_key = "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"


@app.route("/")
def serve_static_index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    prompt = data.get("prompt", "")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 确保使用正确的模型名称
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        answer = response.choices[0].message["content"]
        return jsonify({"answer": answer})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5502)
