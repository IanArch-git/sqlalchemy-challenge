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
        f"List of Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

# Precipitation - query results & conversion
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(measure.date, measure.prcp).all()
    session.close()
    dateprecip_list = []
    for date, prcp in results:
        dpdict = {}
        dpdict["date"] = date
        dpdict["prcp"] = prcp
        dateprecip_list.append(dpdict)
    return jsonify(dateprecip_list)

#Stations - JSON list of stations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations_query = session.query(station.name).all()
    session.close()
    stations_list = list(np.ravel(stations_query))
    return jsonify(stations_list)

#Tobs - query results & JSON list


#Start & Start/End - JSON list, TMIN/TAVG/TMAX for both


if __name__ == "__main__":
    app.run(debug=True)