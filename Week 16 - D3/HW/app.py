# import dependencies
import pandas as pd

from flask import Flask, render_template, jsonify, redirect, current_app

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask_sqlalchemy import SQLAlchemy

engine = create_engine("sqlite:///db/belly_button_biodiversity.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

OTU = Base.classes.otu
SAMPLES = Base.classes.samples
META = Base.classes.samples_metadata

session = Session(engine)

# create instance of Flask
app = Flask(__name__)

db = SQLAlchemy(app)

# create index route
@app.route("/")
def index():
    # return homepage
    return render_template("index.html")

@app.route("/names")
def names():
    results = session.execute("SELECT * FROM samples")
    names = results.keys()
    names = names[1:]
    return jsonify(names)

@app.route('/otu')
def otu():
    results = session.query(OTU.lowest_taxonomic_unit_found).all()
    descriptions = []
    # remove tuples from list
    for result in results:
        descriptions.append(result[0])
    return jsonify(descriptions)

@app.route('/metadata/<sample>')
def metadata(sample):
    split = sample.split('_')
    results = session.query(META.AGE, META.BBTYPE, META.ETHNICITY, META.GENDER, META.LOCATION).filter(META.SAMPLEID == split[1]).all()
    meta = results[0]
    formatted = {
        "AGE": meta[0],
        "BBTYPE": meta[1],
        "ETHNICITY": meta[2],
        "GENDER": meta[3],
        "LOCATION": meta[4],
        "SAMPLEID": split[1]
    }
    return jsonify(formatted)

@app.route('/wfreq/<sample>')
def wfreq(sample):
    split = sample.split('_')
    sample = split[1]
    results = session.query(META.WFREQ).filter(META.SAMPLEID == sample).all()
    formatted = {
        "Wash Frequency" : results[0][0]
    }
    return jsonify(formatted)


@app.route('/samples/<sample>')
def sample(sample):
    results = session.execute("SELECT otu_id," + sample + " FROM samples ORDER BY " + sample + " DESC")

    values = []
    otu_ids = []
    for result in results:
        otu_ids.append(result[0])
        values.append(result[1])

    d = {
        "otu_id" : otu_ids,
        "value": values
    }

    df = pd.DataFrame(d)

    formatted = [{
            "otu_id": df["otu_id"].values.tolist(),
            "value": df["value"].values.tolist()
    }]

    return jsonify(formatted)


    """OTU IDs and Sample Values for a given sample.

    Sort your Pandas DataFrame (OTU ID and Sample Value)
    in Descending Order by Sample Value

    Return a list of dictionaries containing sorted lists  for `otu_ids`
    and `sample_values`

    [
        {
            otu_ids: [
                1166,
                2858,
                481,
                ...
            ],
            sample_values: [
                163,
                126,
                113,
                ...
            ]
        }
    ]
    """


if __name__ == "__main__":
    app.run(debug=True)
