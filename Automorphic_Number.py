n = int(input())
sq = n**2
l=len(str(n))
d = list(str(sq))[-l:]
res = int("".join(map(str, d)))

if n==res:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

