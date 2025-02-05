import numpy as np
#finding determinent
a=np.array([1,2,3,4]).reshape(2,2)
print(a)
print("-------------------------")

#module 'numpy' has no attribute 'det'
#in a submodule named linalg we have det
dt=np.linalg.det(a)
print(dt)

#--------------3-D------------------
a=np.array([1,2,3,4,5,6,7,8]).reshape(2,2,2)
print(a)
dt=np.linalg.det(a)
print(dt)