# iterate on a 1-D array  (ONE BY ONE )
# Iterating means going through elements one by one.


# import numpy as np

# arr = np.array([1, 2, 3])

# for x in arr:
#   print(x)



# Iterating 2-D Arrays
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)
  print(type(x))


#Iterate on each scalar element of the 2-D array:
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]]) #index ke andar index

for x in arr:
  for y in x:   #nextnexted loop 1
    print(y)


# Iterating 3-D Arrays
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:  #nexted loop 2
  for y in x:
    for z in y:
      print(z)



# Iterating Arrays Using nditer()
import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in np.nditer(arr):
  print(x)


# Iterating Array With Different Data Types
# import numpy as np

# arr = np.array([1, 2, 3])

# for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
#   print(x)


# import numpy as np
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)


# Enumerated Iteration Using ndenumerate()

# import numpy as np

# arr = np.array([1, 2, 3])

# for idx, x in np.ndenumerate(arr):
#   print(idx, x)

# Enumerate on following 2D array's elements:

# import numpy as np

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for idx, x in np.ndenumerate(arr):
#   print(idx, x)




