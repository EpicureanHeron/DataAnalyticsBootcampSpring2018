# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
app = Flask(__name__)

# @TODO:  Create a route and view function that takes in a list of strings and renders index.html template
@app.route("/")
def echo():
    l = ["Dog", "Cat", "Bird"]
    return render_template("index.html", list=l)

if __name__ == "__main__":
    app.run(debug=True)
