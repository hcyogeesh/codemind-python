def checkSD(n):
    n1=n
    while(n):
        d = n %10
        if(d==0 or n1%d!=0 ):
            return False
        n=n//10
    return True
    
m= int(input())
n=int(input())

for i in range(m,n+1):
    if(checkSD(i)):
        print(i, end=" ")