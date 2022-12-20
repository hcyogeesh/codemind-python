def isAutomorphic(N):
	if N < 0:
	    N = -N
	sq = N * N
	while (N > 0):
	    if (N % 10 != sq % 10):
	        return False
	    N //= 10
	    sq //= 10
	return True


N = int(input())
if isAutomorphic(N) :
    print ("Automorphic Number")
else:
    print ("Not an Automorphic Number")


