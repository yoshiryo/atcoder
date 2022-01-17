from math import pi, sin, cos

n = int(input())
x0, y0 = map(int, input().split())
xn, yn = map(int, input().split())
midx, midy = (x0+xn)/2, (y0+yn)/2
theta = 2*pi/n

px, py = x0-midx, y0-midy

ansx, ansy = px*cos(theta) - py*sin(theta), px*sin(theta) + py*cos(theta)

ansx += midx
ansy += midy

print(ansx, ansy)