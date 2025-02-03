import numpy as np
#-----------------1-D ndarray---------------
a=np.arange(1,10).reshape(9,)
print(a)
print(a.ndim,a.shape,a.size)
for ind,val in np.ndenumerate(a):
    print(ind[0],"--->",val)

#-----------------2-D ndarray---------------
a=np.arange(21,30).reshape(3,3)
print(a)
print(a.ndim,a.shape,a.size)
for ind,val in np.ndenumerate(a):
    print(ind,"--->",val)

for indval in np.ndenumerate(a):
    print(indval,type(indval))   #tuple
    print("Row:{},col:{}---->Val:{}".format(indval[0][0],indval[0][1],indval[1]))
    print("\n")

#-----------------3-D ndarray---------------
a=np.arange(1,13).reshape(2,2,3)
print(a)
print(a.ndim,a.shape,a.size)
for ind,val in np.ndenumerate(a):
    print(ind,"--->",val)

for indval in np.ndenumerate(a):
    print(indval,type(indval))  #tuple format
    print("Matrix: {} ,Row: {}, col: {}---->Val:{}".format(indval[0][0],indval[0][1],indval[0][2],indval[1]))
    print("\n")