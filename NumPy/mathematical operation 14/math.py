# mathematical operation and functions on Arrays

import numpy as np

arr1 =np.array([30,40,60,20,10])
arr2 =np.array([30,40,60,20,10])
# arr2 =[3]

print(arr1 + arr2)
print(np.add(arr1,arr2))
print(arr1 * arr2)
print(np.multiply(arr1,arr2))
print(arr1 / arr2)
print(np.divide(arr1,arr2))
print(np.power(arr1,arr2))

arr1 =np.array([27,64,8,1])
print(np.sqrt(arr1))