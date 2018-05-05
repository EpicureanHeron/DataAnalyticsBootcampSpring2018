# import dependencies
import pandas as pd

from flask import Flask, render_template, jsonify, redirect, current_app

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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

# @app.route('/otu')
#     """List of OTU descriptions.
#
#     Returns a list of OTU descriptions in the following format
#
#     [
#         "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
#         "Archaea;Euryarchaeota;Halobacteria;Halobacteriales;Halobacteriaceae;Halococcus",
#         "Bacteria",
#         "Bacteria",
#         "Bacteria",
#         ...
#     ]
#     """
#
# @app.route('/metadata/<sample>')
#     """MetaData for a given sample.
#
#     Args: Sample in the format: `BB_940`
#
#     Returns a json dictionary of sample metadata in the format
#
#     {
#         AGE: 24,
#         BBTYPE: "I",
#         ETHNICITY: "Caucasian",
#         GENDER: "F",
#         LOCATION: "Beaufort/NC",
#         SAMPLEID: 940
#     }
#     """
#
# @app.route('/wfreq/<sample>')
#     """Weekly Washing Frequency as a number.
#
#     Args: Sample in the format: `BB_940`
#
#     Returns an integer value for the weekly washing frequency `WFREQ`
#     """
#
# @app.route('/samples/<sample>')
#     """OTU IDs and Sample Values for a given sample.
#
#     Sort your Pandas DataFrame (OTU ID and Sample Value)
#     in Descending Order by Sample Value
#
#     Return a list of dictionaries containing sorted lists  for `otu_ids`
#     and `sample_values`
#
#     [
#         {
#             otu_ids: [
#                 1166,
#                 2858,
#                 481,
#                 ...
#             ],
#             sample_values: [
#                 163,
#                 126,
#                 113,
#                 ...
#             ]
#         }
#     ]
#     """


if __name__ == "__main__":
    app.run(debug=True)
