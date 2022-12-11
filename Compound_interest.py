p,r,t = input().split();

p=float(p)
t=float(t)
r=float(r)

print('%.2f' % (p*pow((1+r/100),t)))