def isPalindrome(s):
    return s == s[::-1]

t=int(input())
while t:
    s=input()
    l =len(s)
    if isPalindrome(s) and l%2==0:
        print("YES EVEN")
    elif isPalindrome(s) and l%2==1:
        print("YES ODD")
    else:
        print("NO")
    
    t=t-1
    