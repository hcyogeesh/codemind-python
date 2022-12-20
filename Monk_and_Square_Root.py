t = int(input())

while (t):
    n,m = map(int, input().split())
    flag=0
    
    for i in range(1, m+1):
        if (n==0):
            i=0;
            flag=1
            break;
        
        if i*i % m ==n:
            flag=1
            break;
            
    if (flag):
        print(i)
    else:
        print("-1")
        
    t=t-1