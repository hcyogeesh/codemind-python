# function that prints binary representation
def bin(digit, n):
   arr = []
   for i in range(digit):
       arr.append(n%2)
       n = n>>1
       
   for i in range(digit-1, -1, -1):
       print(arr[i],end="")
       

def generateAllBin(n):
   high = int(pow(2, n))
   for i in range(high):
       bin(n, i)
       print()
       
n=int(input())       
generateAllBin(n)