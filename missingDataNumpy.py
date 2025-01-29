import numpy as np
data=np.array([1,2,None,3,4])
print(data)

#Replace the missing data with 0
a=np.where(data==None,0,data)
print(a)


#using extract, removing missing values
a=np.extract(data!=None,data)
print(a)