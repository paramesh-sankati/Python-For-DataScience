''' 
    nditer() is used to get individual vals from a ndarray in less time complexity O(N)
    Syntax: for val in np.nditer(ndarray)

'''
import numpy as np
#---------------1-D-------------------------
a=np.random.randint(1,10,size=(6,))   #ndarray using random nums
print(a)
#as it  is 1-D ndarray using single loop
for i in np.nditer(a):
    print(i)


#---------------2-D ndarray----------------
a=np.random.randint(1,100,size=(3,4))
print(a)

#using nditer()
for val in np.nditer(a):
    print(val)


#---------------3-D ndarray----------------
a=np.arange(12).reshape(2,3,2)
print(a)
print(a.ndim,a.shape,a.size)

#using nditer()
for val in np.nditer(a):
    print(val)


#----------------4-D ndarray----------------
a=np.arange(24).reshape(2,2,3,2)
print(a)
print(a.ndim,a.shape,a.size)

#using nditer()
for val in np.nditer(a):
    print(val)