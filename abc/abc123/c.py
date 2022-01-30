import math

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

mi = min(a, b, c, d, e)
g = math.ceil(n/mi)

print(4+g)
