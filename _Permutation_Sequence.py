def getPermutation(n, k):
    fact=1
    numbers=[]
    ans=""
    for i in range(1,n):
        fact=fact*i
        numbers.append(i)
    numbers.append(n) 
    k=k-1
    while(True):
        ans = ans + str(numbers[ k//fact ])
        numbers.pop( k//fact )
        if len(numbers)==0:
            break
        k=k%fact   
        fact=fact//len(numbers)
    return ans 

n,k = map(int, input().split())
print(getPermutation(n,k))
