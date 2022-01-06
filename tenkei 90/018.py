import math 
t = int(input())
l, x, y = map(int, input().split())
r = l / 2
q = int(input())
p = math.pi
for _ in range(q):
    e = int(input())
    theta = 2 * p * e / t
    ye = - r * math.sin(theta)
    ze = r - r * math.cos(theta)
    d = (x**2 + (y - ye)**2) ** 0.5
    dep = math.atan2(ze, d)
    print(math.degrees(dep))