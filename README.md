# SQL Alchemy Homework


## Step 1 - Climate Analysis and Exploration

* Used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. 
* Used the provided starter notebook and hawaii.sqlite files to complete the climate analysis and data exploration for the dates of my trip 9/22-9/30.
* Used SQLAlchemy create_engine to connect to the sqlite database.
* Used SQLAlchemy automap_base() to reflect the tables into classes and save a reference to those classes called Station and Measurement.

### Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.
* Loaded the query results into a Pandas DataFrame
* Plotted the results using the DataFrame plot method.


### Station Analysis

* Designed a query to calculate the total number of stations.
* Designed a query to find the most active stations, listed the stations and counts in descending order.
  * Station USC00519281 has the highest number of observations

* Designed a query to retrieve the last 12 months of temperature observation data (tobs) for the stationwith the highest number of observations and plotted the results as a histogram with `bins=12`.

## Step 2 - Climate App

Designed a Flask API based on the queries above.

* Used FLASK to create the following routes:

### Routes

* `/`

  * Home page.

* `/api/v1.0/precipitation`

  * Returns the JSON representation of the last 12 months of precipitation for the most active station.

* `/api/v1.0/stations`

  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  
  * Returns a JSON list of Temperature Observations (tobs) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
