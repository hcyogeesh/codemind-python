
def countCharacterType(str, c):
    count = 0
    for i in range(0, len(str)):
	    ch = str[i]
	    if (ch==c):
		    count += 1
    if count:
	    print(count)
    else:
        print("-1")



# Driver function.
str = input()
ch=input()
countCharacterType(str,ch)

