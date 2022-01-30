w, h, x, y = map(int, input().split())
a = w/2
b = h/2

if a == x and y == b:
    print(w*h/2, 1)
else:
    print(w*h/2, 0)