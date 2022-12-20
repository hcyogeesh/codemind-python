def hcf(a, b):
	if(b == 0):
		return a
	else:
		return hcf(b, a % b)

a,b = map(int, input().split())

print(hcf(a, b))
