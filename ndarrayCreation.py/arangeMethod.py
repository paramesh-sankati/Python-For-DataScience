import numpy as np

#1-D ndarray
n=np.arange(10)  #ndarray with 0 to 9
print(n)

#2-D ndarray
n=np.arange(1,10).reshape(3,3)   #using arange(start,stop)
print(n)
print(n.ndim)

#3-D ndarray
#using arange(start,stop,step)
n=np.arange(1,16,2).reshape(2,2,2)
print(n)