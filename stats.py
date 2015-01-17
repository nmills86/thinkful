#IMPORT PACKAGES

from scipy import stats
import pandas as pd

# READ IN DATA
# NEXT

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

# PROCESS FILE
# First, split the string on the (hidden characters that indicate) newlines
data = data.splitlines() # we could also do data.split('\n')

# Then, split each item in this list on the commas
# the bracketed expression is a list comprehension
data = [i.split(', ') for i in data] 

# CONVERT TO PANDAS
# Now, convert create a pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

# There's no built-in mode method in Python, so we need scipy.stats
from scipy import stats

# Convert Alcohol and Tobacco columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)


tobacco_range=float(max(df['Tobacco']) - min(df['Tobacco']))
alcohol_range=float(max(df['Alcohol']) - min(df['Alcohol']))


# PRINT OUT EVERYTHING
print "Mean weekly household spending on Alcohol is " + str(df['Alcohol'].mean()) +"."
print "Mean weekly household spending on Tobacco is " + str(df['Tobacco'].mean()) +"."

print "Median weekly household spending on Alcohol is " + str(df['Alcohol'].median()) +"."
print "Median weekly household spending on Tobacco is " + str(df['Tobacco'].median()) +"."

print "Modal weekly household spending on Tobacco is " + str(stats.mode(df['Tobacco'])) +"."
print "Modal weekly household spending on Alcohol is " + str(stats.mode(df['Alcohol'])) +"."

print "The range of weekly household spending on Tobacco is " + str(tobacco_range) +"."
print "The range of weekly household spending on Alcohol is " + str(alcohol_range) +"."

print "The variance of weekly household spending on Tobacco is " + str(df['Tobacco'].var()) +"."
print "The variance of weekly household spending on Alcohol is " + str(df['Alcohol'].var()) +"."



















