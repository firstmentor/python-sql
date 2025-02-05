# Arrays Functions search sorting filter

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
# 0 1 2 3 4

x = np.where(arr == 4)

print(x)

#Find the indexes where the values are even:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)
x = np.where(arr%2 == 1)
print(x)


# Search Sorted  -perform binary search in array,and return the index .where the specified value 
# would be inserted to maintain the search order
import numpy as np
 
# arr = np.array([1,6,7,2,3,4])
arr = np.array([2,5,8,9,13])  #binary search in the array DS ascending order

x = np.searchsorted(arr,8)  #7 kaha pe insert hoga
# index number

print(x)


# Search From the Right Side
# import numpy as np

# arr = np.array([6, 7, 8, 9]) # 0 1 2 3 4

# x = np.searchsorted(arr, 7, side='right')

# print(x)

# Multiple Values
import numpy as np

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])  #insert

print(x)

