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
    precip_query = session.query(measure.date, measure.prcp).all()
    session.close()
    precip_list = []
    for date, prcp in precip_query:
        dpdict = {}
        dpdict["date"] = date
        dpdict["prcp"] = prcp
        precip_list.append(dpdict)
    return jsonify(precip_list)

#Stations - JSON list of stations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations_query = session.query(station.name).all()
    session.close()
    stations_list = list(np.ravel(stations_query))
    return jsonify(stations_list)

#Tobs - query results & JSON list
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    tobs_query = session.query(measure.date, measure.tobs).filter(measure.date >= '2016-08-23').filter(measure.station=='USC00519281').all()
    session.close()
    tobs_list = []
    for date, tobs in tobs_query:
        dtdict = {}
        dtdict["date"] = date
        dtdict["tobs"] = tobs
        tobs_list.append(dtdict)
    return jsonify(tobs_list)

#Start - JSON list, TMIN/TAVG/TMAX for both
@app.route("/api/v1.0/start")
def date_start(start):
    session = Session(engine)
    start_query = session.query(func.min(measure.tobs),func.avg(measure.tobs),func.max(measure.tobs)).filter(measure.date >= start).all()
    session.close
    start_list = []
    for min,avg,max in start_query:
        sdict = {}
        sdict["Min"] = min
        sdict["Average"] = avg
        sdict["Max"] = max
        start_list.append(sdict)
    return jsonify(start_list)

#could not get to work show... want to come back and review, I believe code is correct...

#Start/End - JSON list, TMIN/TAVG/TMAX for both
@app.route("/api/v1.0/start/end")
def date_startend(start,end):
    session = Session(engine)
    startend_query = session.query(func.min(measure.tobs),func.avg(measure.tobs),func.max(measure.tobs)).filter(measure.date >= start, measure.date <= end).all()
    session.close
    startend_list = []
    for min,avg,max in start_query:
        sedict = {}
        sedict["Min"] = min
        sedict["Average"] = avg
        sedict["Max"] = max
        startend_list.append(sedict)
    return jsonify(startend_list)

#could not get to work show... want to come back and review, I believe code is correct...

if __name__ == "__main__":
    app.run(debug=True)