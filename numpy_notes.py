# numpy_notes.py

import numpy as np

# List vs Array
my_list = [0,1,2,3,4]
arr = np.array(my_list)
print(my_list)
print(arr)
# Output -
# [0, 1, 2, 3, 4]
# [0 1 2 3 4]

# Arrange
# arange integers, takes in start,stop, and step size
a = np.arange(0,10)
b = np.arange(0,10,2)
print(a)
print(b)
# Output
# [0 1 2 3 4 5 6 7 8 9]
# [0 2 4 6 8]

# Arrays with 0s or 1s
a = np.zeros((3,5))
b = np.ones((2,4))
print(a)
print(b)
# Output
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# Using random integers between limits 0 and 10
a = np.random.randint(0,10, 5)
# 2D array with random integers
b = np.random.randint(0,10,(3,3))
print(a)
print(b)
# Output
# [4 0 3 5 6]
# [[9 6 1]
#  [5 6 3]
#  [6 7 8]]

# Linearly spaced array
a = np.linspace(0,10,6)
b = np.linspace(0,10,21)
print(a)
print(b)
# Output
# [ 0.  2.  4.  6.  8. 10.]
# [ 0.  0.5  1.  1.5  2.  2.5  3.  3.5  4.  4.5  5.  5.5  6.  6.5   7.  7.5  8.  8.5  9.  9.5 10. ]

# Generate same random number multiple times
np.random.seed(101)
arr = np.random.randint(0,100,10)
print(arr)
# Output
# [95 11 81 70 63 87 75  9 77 40]

a = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
print(f"Max = {a.max()}, Min = {a.min()}, Mean = {a.mean()}")
# To get the index location of max and mean
print(f"Max value is at {a.argmax()} and Min value is at a.argmin()")
# Output
# Max = 29, Min = 2, Mean = 12.9
# Max value is at 9 and Min value is at a.argmin()

# Reshape the above (1, 10) array to a (2, 5) matrix
a.reshape(2, 5)
# Output
# array([[ 2,  3,  5,  7, 11],
#        [13, 17, 19, 23, 29]])

# Indexing
a = np.arange(0, 9).reshape(3, 3)
# Output
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# To pick a specific value from the matric - matrix[row_index, col_index]
print(a[1, 2])
# Output
# 5

# Select n entire row
print(a[1,:])
# Select an entire column
print(a[:,0])
# Output
# [3 4 5]
# [0 3 6]

# Masking for filters
print(a > 3)
# Output
# [[False False False]
#  [False  True  True]
#  [ True  True  True]]
print(a[a > 3])
# Output
# [4 5 6 7 8]
