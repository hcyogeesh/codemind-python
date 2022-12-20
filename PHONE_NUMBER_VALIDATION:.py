# Python program to check if
# given mobile number is valid
import re

def isValid(s):
	
	# 1) Begins with 0 or 91
	# 2) Then contains 6,7 or 8 or 9.
	# 3) Then contains 9 digits
	Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
	return Pattern.match(s)


s = input()
if (isValid(s)):
	print ("Valid")	
else :
	print ("Invalid")


# This code is contributed by rishabh_jain
