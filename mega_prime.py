
def checkDigits(n):
	while (n) :
		dig = n % 10
		if not prime(dig):
		    return 0;
		n = n // 10
	return 1

def prime(n):
	if (n == 1):
		return 0
		
	# check for all factors
	i = 2
	while i * i <= n :
		if (n % i == 0):
			return 0
		i = i + 1
	return 1

def isFullPrime(n) :

	return (checkDigits(n) and prime(n))


n = int(input())
if (isFullPrime(n)) :
	print("Mega Prime")
else :
	print("Not Mega Prime")

