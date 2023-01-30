import math
a,b=map(int, input().split())
sum=0
for i in range(a, b+1):
    sum+=math.sqrt(i)
 
print("{:.2f}".format(sum))
    