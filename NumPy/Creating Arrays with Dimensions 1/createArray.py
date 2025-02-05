#Now we will create a numpy ndarray object
#the array object in numpy is call ndarray
#array()
import numpy as np
x =np.array([1,2,3,4,5])
print(x)
print(type(x))

#we can also pass a list ,tuple or any array link object with array().and it
#will be converted to ndarray

import numpy as np
y =np.array((1,2,3,4,5))
print(y)
print(type(y))


#Dimensions in Arrays
#A dimension in arrays is one level of array depth (nested arrays).

#0-D Arrays :-
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

import numpy as np

arr = np.array(42)

print(arr)  #0-d ka  khud ka ek element hota hai


#1-D Arrays common
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

# These are the most common and basic arrays.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])  #different different arguments

print(arr)

#2-D Arrays 
#create a 2-D array containing 2 Arrays with certain
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
# 1 2 3
# 4 5 6

print(arr)
print("Dismension of Array=",arr.ndim)
print("Shape of Array=",arr.shape)


#3-D arrays
#Now we will create a 3-d array with two 2-D array
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)
print("Shape of Array=",arr.shape)
print("Dismension of Array=",arr.ndim)


