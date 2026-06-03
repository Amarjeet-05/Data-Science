from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) 
# now we are using '/' path in html page of index.html to define form path
# for form submiting we have to use POST requeste and GET for website accessing

def home():
    if request.method == "POST":
        print(request.form) # now this gives the user's entered email and password in key value pair
        email = request.form['email'] #here in ['email'] we have to write the name of the input tag which we specified in html pages
        password = request.form['password']
        print(f"The email is {email} and password is {password}")
        return "<b>Successfully logged in!</b>"
    return render_template("index.html")

# but in general we are not printing the user detail instead we have to store it in on database

app.run(debug=True)