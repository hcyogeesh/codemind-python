

nterms = int(input(""))

n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("")
# if there is only one term, return n1
elif nterms == 1:
    print(n1)
# generate fibonacci sequence
else:
    while count < nterms:
       print(n1, end=" ")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1