import math
limit=10000000
sum=0
for i in range(1,limit):
    sum=sum+(1/i**2)
sum=math.sqrt(sum*6)
print(sum)