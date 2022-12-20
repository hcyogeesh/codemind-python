
from math import sqrt

def isPrime(N):
	k = int(sqrt(N)) + 1
	for i in range(2, k, 1):
		if (N % i == 0):
			return False
		
	return True

def getDifference(N):
    if (N == 0):
        return N
    elif (N == 1):
        return N
    elif (isPrime(N)):
        return N
    aboveN = -1
    belowN = -1
    n1 = N + 1
    while (True):
        if (isPrime(n1)):
            aboveN = n1
            break
        else:
            n1 += 1
    
    n1 = N - 1
    while (True):
        if (isPrime(n1)):
            belowN = n1
            break
        else:
            n1 -= 1
    diff1=aboveN-N
    diff2=N-belowN
    
    if diff1<diff2:
        return aboveN
    elif diff1==diff2:
        return belowN
    else:
        return belowN
	


t = int(input())
while(t):
    n=int(input())
    print(getDifference(n))
    t=t-1