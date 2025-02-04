import numpy as np
a=np.array([10,20,30,40,50,60])
print(a)
a=np.delete(a,1)
print(a)

#-------------------2-D-----------------
a=np.array([10,20,30,40,60,70]).reshape(3,2)
print(a)
a=np.delete(a,1,axis=0)    #deleting row elements at index 1
print(a)

#deleting col elements at index 
a=np.delete(a,1,axis=1)
print(a)