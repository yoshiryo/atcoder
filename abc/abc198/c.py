import math

r, x, y = map(int, input().split())
d = math.sqrt(x**2 + y**2)

if d == r:
    print(1)
elif d > r:
    if d%r == 0:
        print(int(d//r))
    else:
        print(int(d//r + 1))
else:
    print(2)