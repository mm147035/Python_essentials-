# This program uses the NumPy library to perform matrix multiplication.

import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiply the matrices using the dot() method
C = np.dot(A, B)

# Print the result
print(C)
