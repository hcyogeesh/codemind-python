n=int(input())
l=[int(i) for i in input().split()]
c=0
for i in l:
    if i%2!=0:
        c+=1
if c>2:
    print("NO")
else:
    print("YES")