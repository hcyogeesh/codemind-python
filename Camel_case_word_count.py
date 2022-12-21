
def countWords(str):
	count = 1
	for i in range(1, len(str) - 1):
		if (str[i].isupper()):
			count += 1

	return count


str = input()
print(countWords(str))

