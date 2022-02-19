x, y = map(int, input().split())
if x > y:
    print(x, 2*x + y)
elif x < y:
    print(x + 2*y, y)
else:
    if x == 0 and y == 0:
        print(1, 1)
    else:
        print(-1)
