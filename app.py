from flask import Flask, request

app = Flask(__name__)

questions = [
    ["what is the speed of sound in air?", "343"],
    ["what is the formula of calcium oxide?", "cao"],
    ["functional unit of kidney?", "nephron"],
    ["sum of angles of triangle?", "180"],
    ["who led non cooperation movement?", "mahatma gandhi"]
]

@app.route("/")
def home():
    return "<h2>Welcome</h2><a href='/quiz'>Start Quiz</a>"


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        score = 0

        for i in range(len(questions)):
            user = request.form.get(f"q{i}", "").lower().strip()

            if user == questions[i][1]:
                score += 1

        return f"""
        <h2>Your Score: {score}/{len(questions)}</h2>
        <a href='/quiz'>Play Again</a><br>
        <a href='/'>Home</a>
        """

    # Show questions
    html = "<h2>Quiz</h2><form method='POST'>"

    for i, q in enumerate(questions):
        html += f"<p>{q[0]}</p>"
        html += f"<input type='text' name='q{i}'><br><br>"

    html += "<button type='submit'>Submit</button></form>"

    return html


if __name__ == "__main__":
    app.run(debug=True)