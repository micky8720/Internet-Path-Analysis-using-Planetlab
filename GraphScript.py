import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Name of the file')


num_bins = 20


counts, bin_edges = np.histogram(data, bins=num_bins, normed=True)


cdf = np.cumsum(counts)


plt.plot(bin_edges[1:], cdf)

plt.show()