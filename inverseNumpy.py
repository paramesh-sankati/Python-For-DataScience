import numpy as np
a=np.array([2,3,4,5]).reshape(2,2)
print(a)
#inverse of a
b=np.linalg.inv(a)
print(b)