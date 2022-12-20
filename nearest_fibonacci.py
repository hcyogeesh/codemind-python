def nearestFibonacci(num):
	if (num == 0):
		print(0)
		return
	first = 0
	second = 1

	third = first + second

	while (third <= num):

		first = second
		second = third
		third = first + second

	
	if (abs(third - num) >	abs(second - num)):
		print(second)
	elif (abs(third - num) == abs(second - num)):
		print(second, third)
	else:
		print(third)
		
if __name__ == '__main__':
	
	N = int(input())
	nearestFibonacci(N)


