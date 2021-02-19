# numpy_notes.py

import numpy as np

# Reshape the above (1, 10) array to a (2, 5) matrix
a.reshape(2, 5)
# Output
# array([[ 2,  3,  5,  7, 11],
#        [13, 17, 19, 23, 29]])



# Masking for filters
print(a > 3)
# Output
# [[False False False]
#  [False  True  True]
#  [ True  True  True]]
print(a[a > 3])
# Output
# [4 5 6 7 8]
