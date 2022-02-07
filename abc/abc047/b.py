w, h, n = map(int, input().split())
xl = 0
xr = w
yd = 0
yu = h
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        xl = max(xl, x)
    elif a == 2:
        xr = min(xr, x)
    elif a == 3:
        yd = max(yd, y)
    else:
        yu = min(yu, y)
if xl >= xr or yd >= yu:
    print(0)
else:
    print((xr - xl)*(yu - yd))