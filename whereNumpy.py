import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
ind=np.where(a%2==0)
print(ind[0])   #prints indices of 2 multiples

for i in ind[0]:
    print(a[i],end=" ")    #multiples of 2