import numpy as np 
np.random.seed(100)
mat =np.random.randint(1,21,9).reshape(3,3)
#1 se 20 tak 9 value gen karega=
print(mat)
# mat1 =np.sum(mat)
# mat1 =np.min(mat)
# mat1 =np.max(mat)
# mat1 =np.max(mat,axis=0)  #1 row 
# mat1 =np.sum(mat,axis=0)
mat1 =np.cumsum(mat)  #axis=1
print(mat1)


