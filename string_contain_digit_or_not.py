
def countCharacterType(str):
    count = 0
    for i in range(0, len(str)):
        ch=str[i]
        if ch >='0' and ch <= '9':
	        count += 1
    
    if count:
	    print("Contains", count, "digit")
    else:
        print("Doesn't contain digit")




str = input()

countCharacterType(str)

