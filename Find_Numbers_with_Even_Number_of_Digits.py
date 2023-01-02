n=int(input())

l=list(map(int,input().split()))
count=0
for i in l:
    le=len(str(i))
    if le%2==0:
        count+=1
print(count)