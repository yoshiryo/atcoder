w, a, b = map(int, input().split())
d = abs(a - b)
if d <= w:
    print(0)
else:
    print(d - w)