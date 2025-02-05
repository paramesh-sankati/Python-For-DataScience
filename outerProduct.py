import numpy as np
a=np.array([1,3,5,2]).reshape(2,2)
b=np.array([4,2,5,6]).reshape(2,2)

c=np.outer(a,b)
print(c)
 
#inner Product
c=np.inner(a,b)
print(c)
