import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
print(a)

#get vals more than 20 with extract
res=np.extract(a>5,a)
print(res)

#get even Nums
even=np.extract(a%2==0,a)
print(even)

#get odd nums
odd=np.extract(a%2!=0,a)
print(odd)