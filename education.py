from bs4 import BeautifulSoup
import requests
import sqlite3 as lite
import pandas as pd
import matplotlib.pyplot as plt


url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)

soup = BeautifulSoup(r.content)

table_data=soup('table')[6]

j=0
list_of_rows=[]
for row in soup('table')[6].find_all('tr'):
	list_of_cells=[]
	for cell in row.findAll('td'):
		list_of_cells.append(cell.string)
	list_of_rows.append(list_of_cells)

#[7:8] is end
#[191:192] is end

real_data=list_of_rows[8:191]
countries=()
for i in real_data:
	string=(unicode(i[0]), str(int(i[1])), str(int(i[4])), str(int(i[7])),)
	countries=countries + (string,) 

con = lite.connect('un_data.db')
cur = con.cursor()

with con:
    cur.execute('DROP TABLE IF EXISTS ed_expect')
    cur.execute('CREATE TABLE ed_expect (country_name TEXT PRIMARY KEY, year INT, male_exp INT, female_exp INT)')
    cur.executemany('INSERT INTO ed_expect VALUES(?, ?, ?, ?)', countries)

df = pd.read_sql_query("SELECT * FROM ed_expect",con) # WHAT IS THIS?

df['male_exp'].hist()
plt.show()

df['female_exp'].hist()
plt.show()

# Mean and Median Male Exp
print str(df['male_exp'].mean())
print str(df['male_exp'].median())

# Female EXP
print str(df['female_exp'].mean())
print str(df['female_exp'].median())

#cd "C:\Users\Nick\Documents\Thinkful"

import csv
import math
import statsmodels.api as sm
import numpy as np

with open('ny.gdp.mktp.cd_Indicator_en_csv_v2.csv','rU') as inputFile:
    next(inputFile) # skip the first two lines
    next(inputFile)
    header = next(inputFile)
    inputReader = csv.reader(inputFile)
    with con:
        cur.execute('DROP TABLE IF EXISTS gdp')
        cur.execute('CREATE TABLE gdp (country TEXT PRIMARY KEY, _1999 INT, _2000 INT, _2001 INT, _2002 INT, _2003 INT, _2004 INT, _2005 INT, _2006 INT, _2007 INT, _2008 INT, _2009 INT, _2010 INT)')
    for line in inputReader:
    	with con:
    		cur.execute('INSERT INTO gdp (country, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[43:-5]) + '");')

df2 = pd.read_sql_query("SELECT country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010, male_exp, female_exp, year FROM gdp INNER JOIN ed_expect ON gdp.country=ed_expect.country_name;",con) # WHAT IS THIS?

# TRANSPOSE
df3 = pd.melt(df2, id_vars=['country_name', 'male_exp', 'female_exp', 'year'], value_vars=['_1999','_2000','_2001','_2002','_2003','_2004','_2005','_2006','_2007','_2008','_2009','_2010'],var_name='gdp_year',value_name='gdp')
df3['gdp_year']=df3['gdp_year'].map(lambda x: int(x[1:]))
# ONLY KEEP ROWS WHERE GDP YEAR = EXPECTANCY YEAR
df4=df3[df3.year==df3.gdp_year]
df5=df4.dropna(subset=['gdp'], how='all')

df4['gdp'].fillna('missing')


#EXTRACT DATA
df4['gdp'].apply(np.float32)
log_gdp=(df4['gdp'])
log_gdp=math.log(float(log_gdp))
m_exp=df4['male_exp']
f_exp=df4['female_exp']


y=np.matrix(log_gdp).transpose()
x1=np.matrx(m_exp).transpose()
x2=np.matrix(f_exp).transpose()

X1=sm.add_constant(x1)
X2=sm.add_constant(x2)

# RUN THE MODEL, and EXTRACT FIT STATISTICS, MALE
model = sm.OLS(y,X1)
f = model.fit()

# PRINT OUT RESULTS
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

# RUN THE MODEL, and EXTRACT FIT STATISTICS, FEMALE
model = sm.OLS(y,X2)
f = model.fit()

# PRINT OUT RESULTS
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared









