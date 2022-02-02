a, b, c, x, y = map(int, input().split())
ab = a+b
if ab <= 2*c:
    print(a*x + b*y)
else:
    if x >= y:
        print(min(2*c*y + (x-y)*a, 2*c*x))
    else:
        print(min(2*c*x + (y-x)*b, 2*c*y))
