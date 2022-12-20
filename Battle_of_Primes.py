def isPrime(n):
    if n > 1:
    	for i in range(2, int(n/2)+1):
    		if (n % i) == 0:
    			return False
    			break
    	else:
    		return True
    
    else:
    	return False

n1=int(input())
n2=int(input())
n=n1+n2+1
count=1
while(True):
    if isPrime(n):
        print(count)
        break
    else:
        n+=1
        count+=1