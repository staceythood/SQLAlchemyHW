# SQLAlchemyHW
SQL Alchemy Homework

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
  * Station  has the highest number of observations

* Designed a query to retrieve the last 12 months of temperature observation data (tobs) for the stationwith the highest number of observations and plotted the results as a histogram with `bins=12`.

