#the process of converting multidimension ndarray into 1-D ndarray is flatten and also ravel
#viewed obj has base where as copied obj doesnt have base
import numpy as np
a=np.random.randint(10,20,size=(2,3,3))
print(a)
print("Dimension:",a.ndim)
print("shape:",a.shape)

#flatten the 3-d arrayobj into 1-D
#varname=ndarrayObj.flatten()
b=a.flatten()
print(b)

#ravel the 3-D arrayobj into 1-D 
#varname=ndarrayObj.flatten()
c=a.ravel()
print(c)

#difference
print("base of flattened object(copied object)=",b.base)
print("base of raveled object(viewed object)=",c.base)