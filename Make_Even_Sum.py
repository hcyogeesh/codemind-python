n=int(input())
a=list(map(int,input().split()))
s=sum(a)
if s%2==0:
    print(1)
else:
    print(0)