import requests
import sqlite3 as lite
import datetime
import collections
import pandas as pd

api_key = '1a79c9dc9876b90fa38acafc7c783622'
url = 'https://api.forecast.io/forecast/' + api_key + '/'

cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
        }

end_date = datetime.datetime.now() # by setting this equal to a variable, we fix the calculation to the point when we started the scrip (rather than have things move aroudn while we're coding.)

con = lite.connect('weather.db')
cur = con.cursor()
cities.keys()
with con:
	        cur.execute('DROP TABLE IF EXISTS daily_temp')
    		cur.execute('CREATE TABLE daily_temp ( day_of_reading INT, Atlanta REAL, Austin REAL, Boston REAL, Chicago REAL, Cleveland REAL);') #use your own city names instead of city1...

query_date = end_date - datetime.timedelta(days=30) #the current value being processed

with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%Y%m%d')),))
        query_date += datetime.timedelta(days=1)

for k,v in cities.iteritems():
    query_date = end_date - datetime.timedelta(days=30) #set value each time through the loop of cities
    while query_date < end_date:
        #query for the value
        r = requests.get(url + v + ',' +  query_date.strftime('%Y-%m-%dT12:00:00'))

        with con:
            #insert the temperature max to the database
            cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%Y%m%d'))

        #increment query_date to the next day for next operation of loop
        query_date += datetime.timedelta(days=1) #increment query_date to the next day


df = pd.read_sql_query("SELECT * FROM daily_temp",con) 

# Descriptives

# Austin has highest average,  biggest range, and most variaibility
print df.mean()
print df.max()-df.min()
print df.std()*df.std() 

# CALCULATE CHANGE
temp_change = collections.defaultdict(int)
for col in df.columns:
    city_temps = df[col].tolist()
    city_id=col
    city_change = 0
    for k,v in enumerate(city_temps):
        if k < len(city_temps) - 1:
            city_change += abs(city_temps[k] - city_temps[k+1])
    temp_change[city_id] = city_change #convert the station id back to integer

# AUSTIN has most variability
temp_change



