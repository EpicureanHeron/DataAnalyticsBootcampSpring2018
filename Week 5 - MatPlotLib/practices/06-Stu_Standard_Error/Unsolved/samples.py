# Dependencies
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats


# Read and shuffle data
housing_data = pd.read_csv("../Resources/housing_data.csv")
housing_data = housing_data.sample(frac=1).reset_index(drop=True)

# Create a bunch of samples, each with div items
div = 20
lim = len(housing_data) // div
samples = [housing_data.iloc[(i * div):(i * div + div), 13]
           for i in range(0, lim)]

means = []
sem = []
for sample in samples:
    means.append(np.mean(sample))
    sem.append(stats.sem(sample))

x_axis = np.arange(0,25,1)
#plt.plot()
plt.errorbar(x_axis,means,yerr=sem, fmt='o')
plt.show()
