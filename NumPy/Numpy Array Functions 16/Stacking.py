import numpy as np 
a =np.array([1,2,3])
b =np.array([4,5,6])
c =np.array([7,8,9])
arr =np.hstack((a,b,c))  #horizontal
arr =np.vstack((a,b,c))  #vertical
print(arr)


np.random.seed(112)
a =np.random.randint(1,30,9).reshape(3,3)
b =np.random.randint(1,30,9).reshape(3,3)

print(a)
c = np.hstack((a,b))
c = np.vstack((a,b))

print(c)
