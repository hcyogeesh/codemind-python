s=input()
n=int(input())
c=0
for i in s:
    if i=='a':
        c+=1
c1=c*(n//len(s))
for i in range(n%len(s)):
    if s[i]=="a":
        c1+=1
print(c1)