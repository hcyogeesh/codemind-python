n = int(input())
s = input()
data = 0
for i in range(0,n-1):
    data += abs(int(s[i+1])-int(s[i]))
data = n-1-data
if data % 3 == 0 :
    print("Sudhir")
else:
    print("Ashok")