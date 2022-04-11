from math import sin, cos, atan2
a, b = map(int, input().split())
theta = atan2(a, b)
print(sin(theta), cos(theta))