# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
app = Flask(__name__)

# @TODO:  Create a route and view function that takes in a string and renders index.html template
@app.route("/")
def echo():
    user_input = input("What would you like to say?: ")
    return render_template("index.html", text=user_input)

if __name__ == "__main__":
    app.run(debug=True)
