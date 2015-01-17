# IMPORT DATA
import string
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

# READ DATA
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#CLEAN DATA
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: float(str(x)[:-1]))
loansData['FICO.Score.Low'] = loansData['FICO.Range'].map(lambda x: float(str(x)[0:3]))
loansData['FICO.Score.High'] = loansData['FICO.Range'].map(lambda x: float(str(x)[4:7]))


# EXTRACT DATA FOR sm.OLS FUNCTION
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score.Low']

# PREP DATA FOR sm.OLS FUNCTION
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
x = np.column_stack([x1,x2])
X = sm.add_constant(x)


# RUN THE MODEL, and EXTRACT FIT STATISTICS
model = sm.OLS(y,X)
f = model.fit()

# PRINT OUT RESULTS
print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared


#for x in list(loansData['Interest.Rate']):
#	a=string.find(x,'%')
#	b=float(x[:a])
#	c.append(b)

#p = loansData['FICO.Score.Low'].hist()


#a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))