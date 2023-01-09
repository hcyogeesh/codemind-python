t=int(input())

for k in range(t):
    D, d, p,q=map(int, input().split())
   
    n1=D//d
    n2=D%d
    s=0;
    for i in range(n1):
            s+=(p+i*q)*d
        
    s+=(p+n1*q)*n2
    print(s)