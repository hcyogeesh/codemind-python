
def countCharacterType(str):
	vowels = 0
	consonant = 0
	specialChar = 0
	digit = 0

	for i in range(0, len(str)):
		
		ch = str[i]

		if ( (ch >= 'a' and ch <= 'z') or
			(ch >= 'A' and ch <= 'Z') ):

			# To handle upper case letters
			ch = ch.lower()

			if (ch == 'a' or ch == 'e' or ch == 'i'
						or ch == 'o' or ch == 'u'):
				vowels += 1
			else:
				consonant += 1
		
		elif (ch >= '0' and ch <= '9'):
			digit += 1
		else:
			specialChar += 1
	
	print("Vowels:", vowels)
	print("Consonants:", consonant)
	print("Digits:", digit)
	print("White spaces:", specialChar)


# Driver function.
str = input()
countCharacterType(str)

