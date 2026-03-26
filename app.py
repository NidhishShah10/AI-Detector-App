from flask import Flask, render_template, request
from detector import detect_ai
from rephraser import rewrite_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    rewritten = None

    if request.method == "POST":
        essay = request.form["essay"]
        result = detect_ai(essay)
        rewritten = rewrite_text(essay)

    return render_template("index.html", result=result, rewritten=rewritten)

if __name__ == "__main__":
    app.run(debug=True) ##end