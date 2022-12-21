import re
str = input()

sum=0

res = re.findall('[0-9]+', str)

for i in res:
    i=int(i)
    while(i>0):
        
        sum+=i%10
        i=i // 10
    
print(sum)