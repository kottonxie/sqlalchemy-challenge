# Import the dependencies.
# import numpy as np

# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classses.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )


# @app.route("/api/v1.0/precipitation")
# def index():
#     return "Hello, world!"

# @app.route("/api/v1.0/stations")
# def index():
#     return "Hello, world!"

# @app.route("/api/v1.0/tobs")
# def index():
#     return "Hello, world!"

# @app.route("/api/v1.0/<start>")
# def index():
#     return "Hello, world!"

# @app.route("/api/v1.0/<start>/<end>")
# def index():
#     return "Hello, world!"