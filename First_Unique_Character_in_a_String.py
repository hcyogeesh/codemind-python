
string = input()
index = -1
ind=-1
fnc = ""
for i in string:
	if string.count(i) == 1:
		fnc += i
		ind=string.index(i)
		break
	else:
		index += 1
if index == 1:
	print("-1")
else:
	print(ind)
