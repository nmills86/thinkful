# IMPORT DATA
import string
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import pandas as pd
import collections
import math as math

# READ DATA
df = pd.read_csv('C:\Users\Nick\Documents\Thinkful\LoanStats3b.csv',skiprows=1,skipfooter=4,engine='python')

# converts string to datetime object in pandas:
df['issue_d_format'] = pd.to_datetime(df['issue_d']) 
dfts = df.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year*100+x.month).count()
loan_count_summary = year_month_summary['issue_d']

pd.Series.plot(loan_count_summary)
plt.show()
#The series is not stationary. Maybe try first-differencing?

fdiff=np.diff(loan_count_summary)
plt.plot(fdiff)
plt.show()

# This helps 

#PLOT ACF AND PACF
sm.graphics.tsa.plot_acf(fdiff)
plt.show()
# Doesn't seem to be seasonality. Autocorrelation is not decaying. Maybe log the variable?
sm.graphics.tsa.plot_pacf(fdiff)
plt.show()
# Maybe add moving average? partial correlation not decaying either. 


































