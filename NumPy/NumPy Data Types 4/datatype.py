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

# arr = np.array([1, 2, 3, 4])  #int32 1 value 8 byte numpy
# arr = np.array(['apple', 'banana', 'cherry'])  #U^
# arr = np.array([1, 2, 3, 4], dtype='S')  # [b'1' b'2']
# arr = np.array([1, 2, 3, 4], dtype='i4')   #4 byte  8*4 int32
#A non integer string like 'a' can not be converted to integer (will raise an error):
arr = np.array(['a', '2', '3'], dtype='i')

#converting data type in existing array -astype()
# arr = np.array([1.1,2.1,3.1,4.1])
# arr =np.array([1,0,4])
# arr1 = arr.astype('i')  #bool
# print(arr1)

print(arr.dtype)  # 1 byte
# print(arr)
# print(arr.dtype)
