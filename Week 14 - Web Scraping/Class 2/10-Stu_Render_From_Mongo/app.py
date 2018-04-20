from flask import Flask, render_template
import pymongo

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.hurricane
collection = db.hurricane

def insert_records():
    db.collection.insert_many(
        # @TODO: create a list of dictionaries to insert into the db
        [{
            "QB" : "Ben Rothlisberger",
            "RB" : "Le'Veon Bell",
            "WR" : "Antonio Brown"},
            {
            "QB" : "Dak Prescott",
            "RB" : "Ezekiel Elliott",
            "WR" : "Dez Bryant (Not Anymore)"
        }]
    )

def is_collection_empty():
    is_empty = collection.count() == 0
    return is_empty

def insert_if_empty():
    if is_collection_empty():
        insert_records()


@app.route('/')
def index():
    insert_if_empty()
    # @TODO: write a statement that finds all the items in the db and sets it to a variable
    teams = list(db.collection.find())

    # @TODO: render an index.html template and pass it the data you retrieved from the database
    return render_template('index.html', teams = teams)

if __name__ == "__main__":
    app.run(debug=True)
