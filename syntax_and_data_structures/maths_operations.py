# This program uses the NumPy library to perform mathematical operations on arrays.

import numpy as np

# Create an array of numbers
a = np.array([1, 2, 3, 4, 5])

# Calculate the square of each element in the array
a_squared = np.square(a)

# Calculate the mean of the array
a_mean = np.mean(a)

# Print the squared array and the mean of the original array
print("Squared array:", a_squared)
print("Mean of original array:", a_mean)
