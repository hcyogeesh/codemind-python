n=int(input())
l=[int(i) for i in input().split()]
s=""
x=[]
for i in l:
    s=s+str(i)
b=int(s)+1
while(b!=0):
    rem=b%10
    x.append(rem)
    b=b//10
for i in range(len(x)-1,-1,-1):
    print(x[i],end=" ")