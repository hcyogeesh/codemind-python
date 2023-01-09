import math
ab=int(input())
bc=int(input())
hyp=math.sqrt(ab*ab*1.0+bc*bc*1.0);
hyp/=2;
hab=ab*1.0/2;
angle=math.acos(hab/hyp);
angle=angle*180/3.14;
print("{:.0f}".format(angle));