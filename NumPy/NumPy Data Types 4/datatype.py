# # Data Types in Python

# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j


#Data Types in NumPy
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

import numpy as np

arr = np.array([1, 2, 3, 4])
arr = np.array(['apple', 'banana', 'cherry'])
arr = np.array([1, 2, 3, 4], dtype='S')
arr = np.array([1, 2, 3, 4], dtype='i4')



print(arr.dtype)
print(arr.dtype)
print(arr)
print(arr.dtype)
