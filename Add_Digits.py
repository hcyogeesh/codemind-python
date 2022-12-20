import math

def digSum( n):
	sum = 0
	while(n > 0 or sum > 9):
		if(n == 0):
			n = sum
			sum = 0
	
		sum += n % 10
		n //= 10
	
	return sum


n = int(input())
print (digSum(n))

