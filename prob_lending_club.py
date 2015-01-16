# IMPORT DATA

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# READ IN DATA AND DROP NULL VALUES
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

# BOXPLOT
loansData.boxplot(column='Amount.Requested')
plt.savefig("boxplot_lc.png")

# Median amount requested was approximately $10,000, 75th percentile of amount requested was ~$17K, 25th percentile was ~$5K. Not many requested over $30K. 

# HISTOGRAM
loansData.hist(column='Amount.Requested')
plt.savefig("histogram_lc.png")

# Distribution is skewed; Has a long right tail. 

# QQ PLOT
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("qqplot_lc.png")
# QQ Plot shows that the data is not normally distributed. 

#PLOT Amount Requested Against Amount Funded by Requester
# Amount Funded <= Amount Requested

loansData.plot(kind='scatter', x='Amount.Requested', y='Amount.Funded.By.Investors');
plt.savefig("scatter_lc.png")
