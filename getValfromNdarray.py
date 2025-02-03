import numpy as np
a=np.random.randint(1,10,size=(6,))
print(a)
#as it  is 1-D ndarray using single loop
for i in a:
    print(i)

#2-D ndarray
a=np.random.randint(1,100,size=(3,4))
print(a)

#using Loops getting individual vals
for row in a:    #returns a row for each time iterated
    for val in row:
        print(val)


#------------3-D ndarray--------------
a=np.random.randint(1,100,size=(2,2,3))
print(a)