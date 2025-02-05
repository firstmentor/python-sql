import numpy as np 
# arr = np.zeros(5)
# arr = np.zeros((2,3))
# arr1 = np.ones((2,3))
# print(arr)
# print(arr1)


#this function creates an array with all the diagonal elements as 1 nd rest as 0
#(in a square matrix)
arr = np.eye(4) #square
arr = np.eye(3,4)
arr =np.diag([1,2,3])
print(arr)
# print(np.diag(arr))


#randint : this function is used to generate a random number between a given range rand(min,max,total_values)

arr = np.random.randint(1,10,3)
print(arr)

#rand: this function is used to generate a radom values between 0 to 1.
arr = np.random.rand(2,3)  #(2,3)
arr = np.random.randn(2)   #value - mai bhi a skati hai
print(arr)