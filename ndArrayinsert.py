import numpy as np
a=np.array([10,20,30,40,60,70]).reshape(3,2)
print(a)

#inserting  row elements at  1 index
a=np.insert(a,1,[[11,22]],axis=0)
print(a)

#inserting col elements at index 1
a=np.insert(a,1,[[33,23,43,4]],axis=1)
print(a)

#add the row--->[11,12,13,14] at index 1
a=np.insert(a,1,[[11,12,13]],axis=0)
print(a)

#-----------insertion at multiple indices-----------
a=np.insert(a,[0,2],[[10,10,10],[22,22,22]],axis=0)
print(a)

'''a=np.array([10,20,30,40,60,70]).reshape(3,2)
print(a)
a=np.insert(a,[0,2],[[1,2],[5,5]],axis=1)
print(a)'''
