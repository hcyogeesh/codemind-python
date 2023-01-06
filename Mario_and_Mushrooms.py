n = int(input())
state=1

for i in range(1,n+1):
    if state==1:
        state=2
    elif state==2:
        state=-1
    elif state==-1:
        state=1

if state==1:
    print("NORMAL")
elif state==2:
    print("HUGE")
elif state==-1:
    print("SMALL")
    

