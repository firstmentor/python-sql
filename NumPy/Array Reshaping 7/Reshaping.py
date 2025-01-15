# Reshaping :Reshaping means changing the shape of an array.

# import numpy as np
# # Convert the following 1-D array with 12 elements into a 2-D array.
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(4, 3)
# newarr = arr.reshape(2, 3, 2) #Convert the following 1-D array with 12 elements into a 3-D array.
# print(newarr)
# 2 index 1, 2, 3, 4, 5, 6 | 7, 8, 9, 10, 11, 12 (1,2)
# 3 array totega (12 ,34,56) (78, 910 ,11,12)
# 2 element  12  34 56



# Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):


# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(3, 3)

# print(newarr)


# Returns Copy or View?
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# print(arr.reshape(2, 4).base)  #view hai view orignal doc ko show karta hai
# copy hota to shape mai ata

# Unknown Dimension
# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(2, 2, -1)  # -1 Unknown Dimension (2)
# # #newarr = arr.reshape(2, 2, 2)

# print(newarr)

# Flattening the arrays 1-D

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)


