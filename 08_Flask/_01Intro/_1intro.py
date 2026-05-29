from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")         
def hello_world():
    return "<p>Hello Aman!</p>"


@app.route("/about")
def about():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return "<p>This the contact page</p>"

app.run(debug=True)