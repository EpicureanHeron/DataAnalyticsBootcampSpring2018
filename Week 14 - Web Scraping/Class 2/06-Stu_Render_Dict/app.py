# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
app = Flask(__name__)

# @TODO:  Create a route and view function that takes in a list of strings and renders index.html template
@app.route("/")
def echo():
    d = {
        "QB" : "Ben Rothlisberger",
        "RB" : "Le'Veon Bell",
        "WR" : "Antonio Brown"
    }
    return render_template("index.html", dict=d)

if __name__ == "__main__":
    app.run(debug=True)
