n = int(input())
arr = list(map(int,input().split()))
count = 0
min=min(arr)
while min:
    count = 0
    for j in range(0,n):
        if arr[j]%min==0:
            count+=1
    if count==n:
        print(min)
        break
    min-=1