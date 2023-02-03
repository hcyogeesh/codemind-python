n=int(input())
lst=list(map(int, input().split()))

even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    if i%2==1:
        odd.append(i)

even.extend(odd)
print(*even)