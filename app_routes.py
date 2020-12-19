import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from datetime import timedelta
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite copy")

base = automap_base()

base.prepare(engine, reflect = True)

measurement = base.classes.measurement
station = base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route("/")
def home_page ():
    return(
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>")

@app.route("/api/v1.0/precipitation")
def precip():
    previous = dt.date(2017,8,23) - dt.timedelta(days = 365)
    precip = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date >= previous).all()
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations ():
    stations = session.query(station.name, station.station).all()
    return jsonify(stations)
   
@app.route("/api/v1.0/tobs")
def tobs():
    previous_temp = dt.date(2017,8,23) - dt.timedelta(days = 365)
    temp = session.query(measurement.date,measurement.tobs).\
    filter(measurement.station =='USC00519281').\
    filter(measurement.date>=previous_temp).all()
    return jsonify(temp)
       
@app.route("/api/v1.0/<start>")
def temp_start(start):
    results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
    filter(measurement.date >= start).order_by(measurement.date.desc()).all()
    return jsonify(results)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    results1 = session.query(func.min(measurement.tobs), func.avg(measurement.tobs),func.max(measurement.tobs)).\
    filter(measurement.date >= start, measurement.date <= end).order_by(measurement.date.desc()).all()
    return jsonify(results1)

if __name__ == '__main__':
    app.run(debug=True)
