import numpy as np
#x-y+z=2
#2x-y-z=-6
#2x+2y+z=-3
a=np.array([1,-1,1,2,-1,-1,2,2,1]).reshape(3,3)
b=np.array([2,-6,-3])
sol=np.linalg.solve(a,b)
print(sol)
print("x={},y={},z={}".format(sol[0],sol[1],sol[2]))
