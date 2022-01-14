n, a, x, y = map(int, input().split())
if n <= a:
    print(n*x)
else:
    re = n - a
    print(a*x + re*y)