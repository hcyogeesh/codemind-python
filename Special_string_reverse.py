s=input()
l=list(s)
al,sp,si=[],[],[]
for i in range(len(l)):
    if l[i].isalpha():
        al.append(l[i])
    else:
        sp.append(l[i])
        si.append(i)
oput=al[::-1]
for i in range(len(si)):
    oput.insert(si[i],sp[i])
print(*oput,sep='')