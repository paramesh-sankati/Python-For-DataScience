#find the trace of 2-D
import numpy as np
a=np.array([[2,3],[6,1]]).reshape(2,2)
print(a)

tv=np.trace(a)
print(tv)

#-----------3-D-------------
a=np.array([1,2,3,4,5,6,7,8]).reshape(2,2,2)
tv=np.trace(a)
print(tv)