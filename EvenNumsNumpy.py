import  numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])   #ndarray
print(a)
evenNum=a%2==0   #filtering
print(evenNum)    #prints bool vals
print(a[evenNum])

#oddNums
oddNum=a%2!=0
print(a[oddNum])
