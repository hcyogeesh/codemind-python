for i in range(int(input())):
    n,a,b,k=map(int,input().split())
    c=0
    for j in range(1,n+1):
        if k==c:
            break
        if j%a==0 and j%b==0:
           continue
        elif j%a==0 or j%b==0:
           c+=1
    if k<=c:
        print("Win")
    else:
        print("Lose")