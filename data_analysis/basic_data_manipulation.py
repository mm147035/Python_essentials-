# This program demonstrates basic data manipulation and analysis using NumPy.

import numpy as np

# Create a 2D array of random integers between 0 and 10
arr = np.random.randint(0, 10, size=(5, 5))

# Print the array
print("Array:")
print(arr)

# Get the mean, median, and standard deviation of the array
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)

# Print the results
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

# Reshape the array into a 1D array and sort it
flat_arr = arr.flatten()
flat_arr.sort()

# Print the sorted array
print("Sorted Array:")
print(flat_arr)

# Transpose the array
transposed_arr = arr.T

# Print the transposed array
print("Transposed Array:")
print(transposed_arr)
