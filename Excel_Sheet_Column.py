import string

def n2a(n,b=string.ascii_uppercase):
    d, m = divmod(n,len(b))
    return n2a(d-1,b)+b[m] if d else b[m]
   
n = int(input())
 
print (n2a(n-1))
