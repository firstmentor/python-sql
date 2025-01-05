#[start:end]
#[start:end:step]

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
# STEP
print(arr[1:5:2])
print(arr[::2]) #Return every other element from the entire array:
#first value ka har 2 number





# Slicing 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0, 1:4])
# print(arr[1, 1:4])
print(arr[0:2, 2])   #0                    #1
print(arr[0:2, 1:4])






