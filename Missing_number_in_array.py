n=int(input())
for i in range(0,n):
    b=int(input())
    a=list(map(int,input().split()))
    for j in range(1,b+1):
        if j not in a:
            print(j)
            break