import numpy as np
a=np.array([10,20,30,40,60,70]).reshape(3,2)
print(a)

#replacing row 1 elements
print(a[0:1,:])
a[0:1,:]=[[12,23]]
print(a)