def calc(num):
	sums = 0
	product = 1
	while num>0:
		digit = num % 10
		sums = sums + digit
		product = product * digit
		num = num // 10
	
	print(abs(sums-product))
	

# Driver Code
num = int(input())
calc(num)
