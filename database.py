# Assignment 3 for Unit 1

#Import Packages

import sqlite3 as lite
import pandas as pd
import collections

#Connect to Database

con = lite.connect('getting_started.db')

with con:

#DROP Tables

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS weather;")
	cur.execute("DROP TABLE IF EXISTS cities;")

# NEXT
# CREATE & LOAD CITIES
	cur.execute("CREATE TABLE cities(name text, state text)")
	cur.execute("INSERT INTO cities VALUES ('New York City', 'NY')")
	cur.execute("INSERT INTO cities VALUES ('Boston', 'MA')")
	cur.execute("INSERT INTO cities VALUES ('Chicago', 'IL')")
	cur.execute("INSERT INTO cities VALUES ('Miami', 'FL')")
	cur.execute("INSERT INTO cities VALUES ('Dallas', 'TX')")
	cur.execute("INSERT INTO cities VALUES ('Seattle', 'WA')")
	cur.execute("INSERT INTO cities VALUES ('Portland', 'OR')")
	cur.execute("INSERT INTO cities VALUES ('San Francisco', 'CA')")
	cur.execute("INSERT INTO cities VALUES ('Los Angeles', 'CA')")

# CREATE & LOAD WEATHER
	cur.execute("CREATE TABLE weather(city text, year integer, warm_month text, cold_month text, average_high integer)")
	cur.execute("INSERT INTO weather VALUES('New York City', 2013, 'July', 'January', 62)")
	cur.execute("INSERT INTO weather VALUES('Boston', 2013, 'July', 'January', 59)")
	cur.execute("INSERT INTO weather VALUES('Chicago', 2013, 'July', 'January', 59)")
	cur.execute("INSERT INTO weather VALUES('Miami', 2013, 'August', 'January', 84)")
	cur.execute("INSERT INTO weather VALUES('Dallas', 2013, 'July', 'January', 77)")
	cur.execute("INSERT INTO weather VALUES('Seattle', 2013, 'July', 'January', 61)")
	cur.execute("INSERT INTO weather VALUES('Portland', 2013, 'July', 'December', 63)")
	cur.execute("INSERT INTO weather VALUES('San Francisco', 2013, 'September', 'December', 64)")
	cur.execute("INSERT INTO weather VALUES('Los Angeles', 2013, 'September', 'December', 65)")

#Join Data (CITIES WITH WARMEST MONTH IN JULY)
  	cur.execute("SELECT weather.city, cities.state FROM weather INNER JOIN cities ON weather.city=cities.name WHERE weather.warm_month='July'")

#Load Data into panda DATAFRAME
  	rows = cur.fetchall()
  	cols = [desc[0] for desc in cur.description]
  	df = pd.DataFrame(rows, columns=cols)

#Print Cities that have Warmest Month in July
	print "The cities that are warmest in July are: "
	x=1
	for row in rows:
		if x!=6:
			print row[0] + "," + row[1] + ","
		else:
			print "and " + row[0] + "," + row[1] + "."
		x = x + 1

	
