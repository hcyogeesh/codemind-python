x = int(input())
n = list(map(int,input().split()))
s=0
a=0
for i in range(len(n)):
    if i%2==0:
        a+=n[i]
    else:
        s+=n[i]
j = a-s
if j==0:
    print('YES')
else:
    print('NO')