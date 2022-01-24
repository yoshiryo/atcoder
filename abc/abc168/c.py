import math
a, b, h, m = map(int, input().split())
 
s = 30*h + 30*(m / 60)
t = 6*m
pi = abs (s-t)
pi = min(pi, 360-pi)
ans = a**2 + b**2 -2*a*b*math.cos(math.radians(pi))
print(math.sqrt(ans))