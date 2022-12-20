x=int(input())
y=int(input())

sum_x=0
sum_y=0

for each in range(1,x):
    if(x%each==0):
        sum_x=sum_x+each
for i in range(1,y):
    if(y%i==0):
        sum_y=sum_y+i
if(sum_x==y and sum_y==x):
    print("Amicable")
else:
    print("Not Amicable")