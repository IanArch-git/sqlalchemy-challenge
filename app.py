#Dependencies
import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Database Setup - Reflect existing database into new model - Reflect tables - Save
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
measure = Base.classes.measurement
station = Base.classes.station

# Create an app, being sure to pass __name__
app = Flask(__name__)

# Routes
@app.route("/")
def Home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]<br/>"
    )

# Precipitation - query results & conversion


#Stations - JSON list of stations


#Tobs - query results & JSON list


#Start & Start/End - JSON list, TMIN/TAVG/TMAX for both