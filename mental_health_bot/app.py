from flask import Flask, request, jsonify, render_template
from chatbot.logic import get_response
from tests.stress_test import run_stress_test
from tests.anxiety_test import run_anxiety_test
from tests.depression_test import run_depression_test

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    bot_response = get_response(user_input)
    return jsonify({"response": bot_response})

@app.route("/stress-test", methods=["POST"])
def stress():
    answers = request.json.get("answers")
    result = run_stress_test(answers)
    return jsonify({"result": result})

@app.route("/anxiety-test", methods=["POST"])
def anxiety():
    answers = request.json.get("answers")
    result = run_anxiety_test(answers)
    return jsonify({"result": result})

@app.route("/depression-test", methods=["POST"])
def depression():
    answers = request.json.get("answers")
    result = run_depression_test(answers)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
