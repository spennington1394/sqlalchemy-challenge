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

app = Flask(__name__)

@app.route("/")
def home_page ():
    return(
        f"Available Routes: <br/>
        f"/api/v1.0/precipitation:<br/>"
        f"/api/v1.0/stations:<br/>"
        f"/api/v1.0/tobs:<br/>"
        f"/api/v1.0/<start>:<br/>"
        f"/api/v1.0/<start>/<end>")

@app.route("/api/v1.0/precipitation")
def precip():
    previous = dt.date(2017,8,23) - dt.timedelta(days = 365)
    precip = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date >= previous).all()
    
    precipitation = []
    for i in precip:
        dict = {"Date":precip[0], "Precipitation":precip[1]}
        precipitation.append(dict)
    return jsonify(precipitation)
    
    
@app.route("/api/v1.0/stations")
def stations ():
    first1 = session.query(station.name, station.station).all()
    
    stations = []
    for i in first1:
        dict = {"Name": first1[0], "Station Name":first1[1]}
        stations.append(dict)
    
@app.route("/api/v1.0/tobs")
def tobs():
    previous_temp = dt.date(2017,8,23) - dt.timedelta(days = 365)
    temp = session.query(measurement.date,measurement.tobs).\
    filter(measurement.station =='USC00519281',measurement.date>=previous_temp).all()
    
    temps = []
    for e in temps:
        dict = {"Date":temp[0], "Temperature":temp[1]}
        temps.append(dict)
        
@app.route("/api/v1.0/<start>")



@app.route("/api/v1.0/<start>/<end>")
    
    
    
if __name__ == '__main__':
    app.run(debug=True)