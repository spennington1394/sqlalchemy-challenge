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
    precip = session.query(measurement.date, measurement.prcp).filter(measurement.date >= previous).all()
    
    
@app.route("/api/v1.0/stations")
def stations ():
    first1 = session.query(station.name, station.station).all()
    
    
@app.route("/api/v1.0/tobs")
def tobs():
    