import numpy as np
a=np.random.randint(10,25,size=(3,3))
print(a)

#get the elements more than 15
print(a[a>15])      #filtering

#get the elements less than or equal to 15
print(a[a<=15])

#using where function
a=a.reshape(9,)
print(a)
ind=np.where(a>15)
print(ind)
for i in ind[0]:
    print(a[i])