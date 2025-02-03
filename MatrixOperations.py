#Matrix Operations or Arithmatic Operations
import numpy as np
#operators----+,-,*,%,/,//,**
a=np.array([1,2,3,4]).reshape(2,2)
b=np.array([10,20,30,40]).reshape(2,2)


#----------add()---------------
#       syntax:ndobj3=numpy.add(ndobj1,ndobj2)
#       syntax-2: ndObj3=ndObj1+ndObj2
c=np.add(a,b)
print(c)
d=a+b
print(d)

#----------subtract()-----------
c=np.subtract(a,b)
print(c)
d=a-b
print(d)

#----------multiply()-----------
#element wise multiplication
c=np.multiply(a,b)
print(c)
d=a*b               #using operator
print(d)

#row-column wise multiplication
e=np.dot(a,b)
print(e)
#matmul()
f=np.matmul(a,b)
print(f)

#--------------divide()---------------
c=np.divide(a,b)
print(c)
d=a/b   #using operator
print(d) 

#----------floor_divide()---------
c=np.floor_divide(a,b)
print(c)
d=a//b
print(d)
#--------------mod()--------------
c=np.mod(a,b)     #gets remainders 
print(c)
d=a%b
print(d)

#-------------power()--------------
print(a)
print(b)
c=np.power(b,a)
print(c)
d=a**b
print(d)