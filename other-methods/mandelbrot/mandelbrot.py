c=-0.75+0.01j # increase number of 0s in complex part in order to get higher precision 
z=0
steps=1
while z.real < 2:
    steps+=1
    z=z*z+c
print(steps)