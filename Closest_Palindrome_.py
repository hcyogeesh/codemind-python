def isPalindrome(n):
	for i in range(len(n) // 2):
		if (n[i] != n[-1 - i]):
			return False

	return True

def convertNumIntoString(num):

	Snum = str(num)
	return Snum

def closestPalindrome(num):

	RPNum = num - 1
	while (not isPalindrome(
		convertNumIntoString(abs(RPNum)))):
		RPNum -= 1

	SPNum = num + 1
	while (not isPalindrome(
		convertNumIntoString(SPNum))):
		SPNum += 1

	if (abs(num - RPNum) > abs(num - SPNum)):
		print(SPNum)
	elif (abs(num - RPNum) == abs(num - SPNum)):
		print(RPNum, SPNum)
	else:
		print(RPNum)

if __name__ == '__main__':

	num = int(input())

	closestPalindrome(num)

