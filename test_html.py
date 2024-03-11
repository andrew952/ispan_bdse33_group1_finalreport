from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process_input", methods=["POST"])
def process_input():
    data = request.get_json()
    user_input = data["inputText"]
    # 在此处编写您的处理逻辑，将输入分解成逐字列表并生成推荐列表
    # 这里只是一个示例，您需要根据实际需求进行相应修改
    input_list = list(user_input)
    recommend_list = [c.upper() for c in input_list]
    return jsonify({"from_gpt": input_list, "the_recommend": recommend_list})


if __name__ == "__main__":
    app.run(debug=True)
