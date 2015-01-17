# IMPORT DATA
import string
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import math
# READ DATA
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#CLEAN DATA
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: float(str(x)[:-1]))
loansData['FICO.Score.Low'] = loansData['FICO.Range'].map(lambda x: float(str(x)[0:3]))
loansData['FICO.Score.High'] = loansData['FICO.Range'].map(lambda x: float(str(x)[4:7]))

# CREATE NEW VARS
loansData['Rate.Twelve'] = loansData['Interest.Rate']. map(lambda x: float(x)<12)
loansData['Intercept'] = 1

# MAKE LIST OF IVs 
ind_vars = ['Intercept', 'FICO.Score.Low', 'Amount.Requested']

# RUN THE MODEL
logit = sm.Logit(loansData['Rate.Twelve'], loansData[ind_vars])
result = logit.fit()
coeff = result.params 
print coeff


# PREDICTION FUNCTION
def pred(coeff_list, amount, fico):
	intercept=float(list(coeff_list)[0]);
	fico_c=float(list(coeff_list)[1])*fico;
	amt_c=float(list(coeff_list)[2])*amount;


	rhs=-1*(intercept+amt_c+fico_c);
	
	res=1/(1+math.exp(rhs));
	#res=1/(1+(math.exp(-1*(intercept+amt_c+fico_c)));
	if res>=0.7:
		print "Predicted probability of getting loan is " + str(int(res*100)) + "%. Therefore, you are likely to receive a loan of $" + str(amount) + " at an interest rate below 12%.";
	else:
		print "Predicted probability of getting loan is " + str(int(res*100)) + "%. Therefore, you are unlikely to receive a loan of $" + str(amount) + " at an interest rate below 12%.";
	return;
# TEST IT OUT!
pred(coeff,10000,750)
pred(coeff,10000,400)


