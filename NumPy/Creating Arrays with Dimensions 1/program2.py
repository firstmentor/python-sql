import numpy as np
a =[]
n =int(input("Enter Size of the array"))
for i in range(n):
    val =int(input("Enter Number"))
    a.append(val)
myarray =np.array(a)  
print(myarray)  
print(type(myarray))