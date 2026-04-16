from flask import Flask, request

app = Flask(__name__)

# Questions
questions = [
    {"q": "2 + 2 = ?", "ans": "4"},
    {"q": "5 + 3 = ?", "ans": "8"}
]

@app.route("/")
def home():
    return """
    <h1>🧠 Test Start</h1>
    <form action="/quiz" method="post">
        Name: <input name="name"><br><br>
        <input type="submit" value="Start Test">
    </form>
    """

@app.route("/quiz", methods=["POST"])
def quiz():
    return f"""
    <form action="/result" method="post">
        {questions[0]['q']} <input name="q1"><br><br>
        {questions[1]['q']} <input name="q2"><br><br>
        <input type="submit" value="Submit">
    </form>
    """

@app.route("/result", methods=["POST"])
def result():
    score = 0

    if request.form.get("q1") == questions[0]["ans"]:
        score += 1
    if request.form.get("q2") == questions[1]["ans"]:
        score += 1

    return f"<h1>Result: {score}/2</h1>"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)