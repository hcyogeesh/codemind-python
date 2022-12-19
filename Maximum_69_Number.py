
def max69(num):
    str_num = list(str(num))
        
    for i in range(len(str_num)):
	    if str_num[i] == "6":
		    str_num[i] = "9"
		    break

    return int(''.join(str_num))

num=int(input())
print(max69(num))
