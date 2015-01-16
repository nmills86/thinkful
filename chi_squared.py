# IMPORT
from scipy import stats
import collections

# LOAD DATA 
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# CLEAN DATA & TAKE FREQUENCIES
loansData.dropna(inplace=True)
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

#CHI-SQUARE TEST
chi, p = stats.chisquare(freq.values())

# PRINT RESULTS
print "The Chi-Squared Test Statistic is " + str(chi) + "."
print "The p-value from the Chi-Squared Test is " + str(p) + "."