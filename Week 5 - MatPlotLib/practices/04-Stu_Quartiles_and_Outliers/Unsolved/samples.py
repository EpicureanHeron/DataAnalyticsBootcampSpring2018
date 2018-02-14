# Dependencies
import matplotlib.pyplot as plt
import numpy as np



arr = [8, 8, 12, 24, 54, 54, 75, 78, 98, 102, 132]
x_axis = np.arange(0, len(arr), 1)

# Calculate the indices for the lower and upper quartiles
lower_quart_index = (len(arr) + 1) // 4
lower_quart = np.percentile(arr,25, interpolation='midpoint')
median = np.percentile(arr, 50, interpolation='midpoint')
upper_quart = np.percentile(arr, 75, interpolation='midpoint')

# Retrieve the lower and upper quartiles

# Calculate the interquartile range
IQR = upper_quart - lower_quart
# Create axes for the included and excluded data
points = [lower_quart, median, upper_quart]
# Create a plot displaying included and excluded data
plt.plot([.25,.5,.75],points)
plt.title("Lower Quartile, Median, Upper Quartile")
plt.xlabel("Percentile")
plt.ylabel("Value")
plt.show()
# Report descriptions of the data
print("Q1: ")