#Array indexing is the same as accessing an array element.
#start with 0, Second 1

# 1-D-Arrays

# import numpy as np
# arr =np.array([1,2,3,4]) #0 123 4
# print(arr[1])
# print(arr[2] + arr[3])


# Access 2-D Arrays
# import numpy as np

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])   #rows and columns
# 0#1 2 3 4 5  #row 0
# 1#6 7 8 9 10
# #columns
# print('2nd element on 1st row: ', arr[1, 4])
# print(arr[1][4])


#Access 3-D Arrays
import numpy as np

arr = np.array([[[1,2,3,4,5], [6,7,8,9,10]],[[11,12,13,14,15], [16,17,18,19,20]]])   #rows and columns
# 0#1 2 3 4 5 | 6  7 8 9 10  #row 
# 1#11 12 13 14 15 | 16 17 18 19 20
#columns
print('2nd element on 1st row: ', arr[0, 1, 2])
print(arr[1][1][4])


#Negative Indexing
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])