
from math import floor, log2

def minAbsDiff(n) :

	left = pow(2, floor(log2(n)))

	right = left * 2
	return min((n - left), (right - n))


if __name__ == "__main__" :

	n = int(input())
	print(minAbsDiff(n))

