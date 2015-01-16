# IMPORT PACKAGES
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

# READ IN DATA
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

# PRINT FREQUENCIES
c = collections.Counter(x)
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

# MAKE BOXPLOT AND SAVE
plt.boxplot(x)
plt.savefig("boxplot_xdata.png")
# MAKE HISTOGRAM AND SAVE
plt.hist(x, histtype='bar')
plt.savefig("histogram_xdata.png")
# MAKE QQ PLOT AND SAVE
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("qqplot_xdata.png")
