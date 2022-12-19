
from math import *

def SieveOfEratosthenes(n, isPrime) :

	isPrime[0], isPrime[1] = False, False

	for i in range(2, n + 1) :
		isPrime[i] = True

	for p in range(2, int(sqrt(n)) + 1) :

		if isPrime[p] == True :

			for i in range(p * 2, n + 1, p) :
				isPrime[i] = False


def findPrimePair(n) :

	flag = 0

	isPrime = [False] * (n + 1)
	SieveOfEratosthenes(n, isPrime)


	for i in range(2, n) :
		x = int(n / i)

		if (isPrime[i] & isPrime[x] and
			x != i and x * i == n) :
			print(i, x)
			flag = 1
			break

	if not flag :
		print("-1")

if __name__ == "__main__" :

	n=int(input());

	findPrimePair(n)


