import numpy as np
a=np.array([3,1,2,4])
print("Mean=",np.mean(a))

#-----------2-D array-------------
a=np.array([3,1,2,4]).reshape(2,2)
#Find the mean for col and row
m=np.mean(a)
print("mean=",m)
colmean=np.mean(a,axis=0)
print("colMean:",colmean)
rowmean=np.mean(a,axis=1)
print("row Mean:",rowmean)

#-----------3-D array--------------
a=np.array([3,1,2,13,23,4,2,13]).reshape(2,2,2)
#Find the mean for col and row
m=np.mean(a)
print("mean=",m)
colmean=np.mean(a,axis=0)
print("colMean:",colmean)
rowmean=np.mean(a,axis=1)
print("row Mean:",rowmean)