n = int(input())
arr = list(map(int,input().split()))
a = [-1]*max(arr)
for i in range(0,n):
    if a[arr[i]-1]==-1:
        a[arr[i]-1]+=2
    else:
        a[arr[i]-1]+=1
for i in range(len(a)):
    if a.count(-1)==len(a):
        break
    print(a.index(max(a))+1,end=" ")
    a[a.index(max(a))]=-1