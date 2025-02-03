import numpy as np

#Median of a odd number of elements array
a=np.random.randint(1,10,size=9)
print(a)
m=np.median(a)
print("Median:",m)

#Median of a even number of elements array
a=np.random.randint(1,10,size=8)
print("Medain:",np.median(a))

#------------------2-D array--------------------
a=np.random.randint(1,10,size=(2,4))
median=np.median(a)
print(median)

#------row wise and col wise median-------------
colmedian=np.median(a,axis=0)
print("Col Median:",colmedian)
rowmedian=np.median(a,axis=1)
print("Row median:",rowmedian)


