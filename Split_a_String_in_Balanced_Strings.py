s=input()
l,r,c=0,0,0
for i in range(len(s)):
    if s[i]=="R":
        r+=1
    if s[i]=="L":
        l+=1
    if r==l:
        c+=1
print(c)