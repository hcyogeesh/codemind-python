n=int(input())
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s=""
while n>0:
    rem=n%26
    if rem==0:
        s=s+'Z'
        n=(n//26)-1
    else:
        s=s+a[rem-1]
        n=n//26
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")