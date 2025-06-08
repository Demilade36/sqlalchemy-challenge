#Import the dependencies.
import datetime as dt

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect

from flask import Flask, jsonify, json, Response
import numpy as np


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables 
Base.prepare(autoload_with=engine)  

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Calculate the date one year from the last date in data set.
prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return """
    <html>
        <head><title>Hawaii Climate API</title></head>
        <body>
            <h2>Welcome to the Hawaii Climate Analysis API!</h2><br/>
            <p>These are the Available Routes:</p>
            <ul>
                <li>/api/v1.0/precipitation</li>
                <li>/api/v1.0/stations</li>
                <li>/api/v1.0/tobs</li>
                <li>/api/v1.0/temp/&lt;start_date&gt;/</li>
                <li>/api/v1.0/temp/&lt;start_date&gt;/&lt;end_date&gt;/</li>
            </ul>
            <p><strong>Note:</strong> 'start_date' and 'end_date' must be in format YYYY-MM-DD (e.g. 2016-08-01)</p>
        </body>
    </html>
    """

@app.route ('/api/v1.0/precipitation/')
def precipitation():
    """Return the precipitation data as json"""
    session=Session(engine)

    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

    session.close()

    #Dict with date as the key and prcp as the value
    precip = dict(results)
    return jsonify(precip)


# Return a JSON-list of stations from the dataset.
@app.route('/api/v1.0/stations/')
def stations():
    """Return a list of stations"""
    session = Session(engine) 

    station_list = session.query(Station.station)\
    .order_by(Station.station).all() 

    session.close()

    print("Station List:")
    all_stations = list(np.ravel(station_list))
    return jsonify(all_stations)



# Return a JSON-list of Temperature Observations from the dataset.
@app.route('/api/v1.0/tobs/')
def temp():

    """Return a list of Temperatures"""
    session = Session(engine)  

    # Calculate the date one year from the last date in data set.
    # This is part of the Flask set up above

    # Perform a query to retrieve the data and precipitation scores
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    session.close()

    #Dict with date a sthe key and prcp as teh value
    temps = list(np.ravel(results))
    return jsonify(temps)


@app.route ('/api/v1.0/temp/<start_date>/')
def stats(start_date):
    """Return TMIN, TAVG, TMAX"""
    print(f"Received request for start_date: {start_date}")
    session = Session(engine)

    # Select Statement
    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
        

    # Query for the min, avg, max temps for date >= start
    results = session.query(*sel).filter(Measurement.date >= start_date).all()

    session.close()

    # Convert list of tuples into normal list
    start = list(np.ravel(results))
    return jsonify(start)


@app.route('/api/v1.0/temp/<start_date>/<end_date>/')   
def startdate_enddate(start_date, end_date):
    print(f"Received request for start_date: {start_date} and end_date: {end_date}")
    session = Session(engine)

    # Select Statement
    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

    # Query for the min, avg, max temps for date >= start_date and <=end_date
    results = session.query(*sel).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()
    
    # Convert list of tuples into normal list
    startdate_enddate_temps = list(np.ravel(results))
    return jsonify( startdate_enddate_temps)


if __name__ == "__main__":
    app.run(debug=True)