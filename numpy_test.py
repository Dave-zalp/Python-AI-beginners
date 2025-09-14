# NumPy (short for Numerical Python) is a fundamental library in Python used for numerical computing.
# It provides powerful tools for working with arrays, matrices, and mathematical functions—especially for data science,
# machine learning, and scientific computing.

import numpy as np

array = np.array([1, 2, 3, 4])

print(array)

# matrix manipulation

# 1

matrix = np.array([[1, 2], [3, 4]])
print(matrix.dot(matrix, matrix))  # dot means multiplication

# 2
matrix = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[4, 3], [1, 2]])
print(matrix.dot(matrix, matrix_2))
