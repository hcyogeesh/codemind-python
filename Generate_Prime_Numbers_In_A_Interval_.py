# Python program to print all
# prime number in an interval

def prime(x, y):
	prime_list = []
	for i in range(x, y):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				prime_list.append(i)
				print(i)
	return prime_list

# Driver program
starting_range = int(input())
ending_range = int(input())
lst = prime(starting_range, ending_range)
#if len(lst) == 0:
#	print("-1")
#else:
#	print(lst)
