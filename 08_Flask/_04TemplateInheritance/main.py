from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

app.run(debug=True)

# we are using template inheritance which helps to reduce repitative work.
# if we have multiple pages inside the website and all pages are using same html layout 
# only name or content of the page is changed then template inheritance helps to reduce code
# we use base class in all html and change things by using their id name