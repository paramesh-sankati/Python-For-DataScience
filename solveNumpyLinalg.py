#Solve the following linear equations by using solve()
#2x+3y=4
#6x+y=2
import numpy as np
#AX=B 
a=np.array([[2,3],[6,1]])    #coefficients
b=np.array([4,2])            #constants
sol=np.linalg.solve(a,b)
print(sol)

#8x-3y=-3
#5x-2y=-1
a=np.array([8,-3,5,-2]).reshape(2,2)
b=np.array([-3,-1])
sol=np.linalg.solve(a,b)
print(sol)

print("x={},y={}".format(sol[0],sol[1]))