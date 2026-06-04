from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

# Jinja2 is a fast, expressive, and extensible templating engine for Python. 
# It allows developers to embed logic—such as variables, loops, and conditional statements
#  static text or HTML files, making it easy to generate dynamic web pages or configuration files
# we can use python variable in html page by their name(variable name) and we can also
# use html tag in python which can also use in html page by its name 
# it also help to use if-else statement and loop in html page
def about():
    name = "Aman"
    language = "Python"
    luckyno = [1,2,3,5,4,6]
    ptag = "<p>this is html paragraph tag</p>"
    return render_template("index.html", name=name, lang=language, luck=luckyno, ptag= ptag)

app.run(debug=True)