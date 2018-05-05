# import necessary libraries
import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

my_data = []

@app.route("/api/data")
def data():
    return jsonify(my_data)

@app.route("/send", methods=["GET","POST"])
def send():
    if request.method == "POST":
        nickname = request.form["nickname"]
        age = int(request.form["age"])

        form_data = {
            "nickname" : nickname,
            "age" : age
        }
        my_data.append(form_data)
        return "Thanks for the data"

    elif request.method == "GET":
        return render_template("form.html")

@app.route("/")
def home():
    return "Welcome!"

if __name__ == "__main__":
    app.run(debug=True)
