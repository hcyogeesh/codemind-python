a=int(input())
arr=list(map(int,input().split()))
x=y=0
for i in range(a):
    if i%2==0:
        x+=arr[i]
    else:
        y+=arr[i]
if (abs(x-y))%4==0:
    print("X")
else:
    print("Y")