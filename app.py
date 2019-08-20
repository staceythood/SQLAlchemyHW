import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Hawaii Weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date/<start><br/>"
        f"/api/v1.0/start_end/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    # Perform a query to retrieve the data and precipitation
    results = session.query(Measurement.date, Measurement.prcp).order_by(Measurement.date.desc()).filter(Measurement.date >= '2016-08-23').all()
    session.close()

#Convert the query results to a Dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.
    dates_prcp = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["precipitation"] = prcp
        dates_prcp.append(prcp_dict)

    return jsonify(dates_prcp)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    # Perform a query to retrieve the stations 
    results = session.query(Station.station).all()
    session.close()
    # Return a JSON list of stations from the dataset.
    stations = results

    # return jsonify(stations)
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    #query for the dates and temperature observations from a year from the last data point.
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2016-08-23').filter(Measurement.station=='USC00519281').all()
    session.close()
    #Return a JSON list of Temperature Observations (tobs) for the previous year.
    temps = list(np.ravel(results))
    return jsonify(temps)

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
app.route("/api/v1.0/start_date/<start>")
def start(start_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    #When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
    for row in session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all():
        return jsonify(row)
    session.close()

app.route("/api/v1.0/start_end/<start_end>")
def start_end(start_date, end_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    ## When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    session.close()
    
    min_avg_max2=list(np.ravel(results))
    return jsonify(min_avg_max2)

if __name__ == '__main__':
    app.run(debug=True)