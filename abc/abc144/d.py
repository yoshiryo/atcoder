import math

a, b, x = map(int, input().split())

if 2*x<=a*a*b:
    tan = (a*b*b)/(2*x)
else:
    tan = 2*(a*a*b - x)/(a**3)

print(math.degrees(math.atan(tan)))