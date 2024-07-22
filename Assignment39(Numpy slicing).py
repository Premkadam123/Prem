# Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np

# Create an array of 10 zeros
zeros_array = np.zeros(10)

# Create an array of 10 ones
ones_array = np.ones(10)

# Create an array of 10 fives
fives_array = np.full(10, 5)

# Print the arrays
print("Array of 10 zeros:", zeros_array)
print("Array of 10 ones:", ones_array)
print("Array of 10 fives:", fives_array)

# OUTPUT :
# Array of 10 zeros: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Array of 10 ones: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
# Array of 10 fives: [5 5 5 5 5 5 5 5 5 5]
