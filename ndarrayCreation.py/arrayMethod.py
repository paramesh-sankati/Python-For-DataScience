import numpy as np
lst=[1,2,3,4,5,6]
n=np.array(lst)
print(n)
print(type(n))

#reshaping to 2-D array
n=np.array(lst).reshape(2,3)
print(n)
print(n.ndim)  #dimension

#3-D ndarray
n=np.array([1,2,3,4,5,6,7,8]).reshape(2,2,2)
print(n)
print(type(n))
print(n.ndim)