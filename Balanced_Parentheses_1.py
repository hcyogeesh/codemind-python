s=input()
for i in s:
    if i=='(' or i==')' or i=='{' or i=='}' or i=='[' or i==']':
        a=s.count('(')
        b=s.count(')')
        c=s.count('{')
        d=s.count('}')
        e=s.count('[')
        f=s.count(']')
        if a==b and c==d and e==f:
            print("True")
            break
        else:
            print("False")
            break