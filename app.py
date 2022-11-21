from flask import Flask, render_template, request
from cypher import cypher

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/translate", methods=['POST'])
def translate():
    if request.method == 'POST':
        print(request.form)
        if "displacement" in request.form:
            result = cypher(request.form["input_text"], int(request.form["displacement"]))
            return render_template("result.html", res=result)
    return "hello :O"


if __name__ == "__main__":
    app.run()
