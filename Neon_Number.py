def checkNeon (x) :
	sq = x * x
	sum_digits = 0
	while (sq != 0) :
		sum_digits = sum_digits + sq % 10
		sq = sq // 10
	
	return (sum_digits == x)

i = int(input())
if (checkNeon(i)):
    print("Neon Number")
else:
    print("Not Neon Number")
