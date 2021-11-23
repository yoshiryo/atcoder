from math import gcd

n = int(input())
xy = []

for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))

s = set()

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        xi, yi = xy[i]
        xj, yj = xy[j]
        xd, yd = xi - xj, yi - yj
        g = gcd(xd, yd)
        s.add((xd // g, yd // g))
print(len(s))
