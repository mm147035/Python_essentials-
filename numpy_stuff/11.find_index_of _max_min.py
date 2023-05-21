import numpy as np

numbers = np.array([5, 2, 8, 1, 6])

# Index of the maximum value
max_index = np.argmax(numbers)
print(max_index)  # Output: 2

# Index of the minimum value
min_index = np.argmin(numbers)
print(min_index)  # Output: 3
