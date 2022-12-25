n=int(input())
s=[]
s=list(map(int, input().split()))

total=0
for i in range(0,n):
    total=total+s[i]
flag=0
for i in range(n,0,-1):
    if total%i==0:
        print(i)
        flag=1
        break

if flag==0:
    print('0')
