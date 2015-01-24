# IMPORT DATA
import string
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import pandas as pd
import collections

# READ DATA
loansData = pd.read_csv('C:\Users\Nick\Documents\Thinkful\LoanStats3c.csv',skiprows=1,skipfooter=4,engine='python')


# CHECK FOR INVALID VALUES ON home_ownership variable
freq1 = collections.Counter(loansData['home_ownership'])

# KEEP 'RENT', 'MORTGAGE', 'OWN', INSPECT ANY
z=loansData[loansData['home_ownership'] == 'ANY']
print z

# Drop ANY
loansData=loansData[loansData.home_ownership!='ANY' ]

# CLEAN INTEREST RATE VARIABLE
loansData['int_rate'] = loansData['int_rate'].map(lambda x: float(str(x)[:-1]))

# PLOT VARIABLES OF INTEREST
loansData.hist(column='annual_inc')
plt.show()
loansData.hist(column='int_rate')
plt.show()
# SERIOUS INCOME OUTLIERS!!! GUESS I'LL LEAVE THEM IN. 

# PLOT INTEREST RATE AGAINST ANNUAL INCOME
loansData.plot(kind='scatter', x='annual_inc', y='int_rate')
plt.show()
# <1000000
ld2=loansData[loansData.annual_inc<100000]
ld2.plot(kind='scatter', x='annual_inc', y='int_rate')
plt.show()

# NO APPARENT RELATIONSHIP BETWEEN INCOME AND INTEREST RATE

# FIT LINEAR MODEL, y=interest_rate, x=annual_inc
intrate = loansData['int_rate']
inc = loansData['annual_inc']

y = np.matrix(intrate).transpose()
x = np.matrix(inc).transpose()
X = sm.add_constant(x)


# RUN THE MODEL, and EXTRACT FIT STATISTICS
model = sm.OLS(y,X)
f = model.fit()

# PRINT OUT RESULTS
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[0]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

# On average, a $100,000 increase in income decreases the interest rate of the loan by 0.5 percentage points. 

#PLOT INTEREST RATE BY HOMEOWNERSHIP

loansData.boxplot(column='int_rate', by='home_ownership')
plt.show()

# NO DISCERNIBLE RELATIONSHIP BETWEEN INTEREST RATE AND HOMEOWNERSHIP STATUS, I THINK IT'S OK TO TREAT MORTGAGE AND OWN AS ONE GROUP

loansData['own'] = loansData['home_ownership']. map(lambda x: x=="OWN" or x=="MORTGAGE")

# FIT UPDATED LINEAR MODEL, y=interest_rate, x=annual_inc own
intrate = loansData['int_rate']
inc = loansData['annual_inc']
own = loansData['own']

y = np.matrix(intrate).transpose()
x1 = np.matrix(inc).transpose()
x2 = np.matrix(own).transpose()
x = np.column_stack([x1,x2])
X = sm.add_constant(x)

# RUN THE MODEL, and EXTRACT FIT STATISTICS
model = sm.OLS(y,X)
f = model.fit()

# PRINT OUT RESULTS
print 'Coefficients: ', f.params[0:3]
print 'Intercept: ', f.params[0]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

# On average, a $100,000 increase in income decreases the interest rate of the loan by 0.5 percentage points. (Change was at the hundredth decimal)
# On average, applicants who own their home or have a mortgage have an interest rate that's 0.01 percentage points lower. 


# Create Interaction Term
x3 = np.multiply(x1,x2)
x = np.column_stack([x1,x2,x3])
X = sm.add_constant(x)

# RUN THE MODEL AGAIN, AND EXTRACT FIT STATISTICS
model = sm.OLS(y,X)
f = model.fit()

#PRINT OUT RESULTS
print 'Coefficients: ', f.params[0:4]
print 'Intercept: ', f.params[0]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

# On average, a $100,000 increase in income decreases the interest rate of the loan by 0.5 percentage points. (Change was at the hundredth decimal)
# On average, applicants who own their home or have a mortgage have an interest rate that's 0.01 percentage points lower. 
# On average, a $100,000 increase in income, given that you're a homeowner, decreases the interest rate of the loan by 0.46 percentage points. So, this suggests 
# income matters slightly less in the determination of an interest rate if you are a home-owner. 


























