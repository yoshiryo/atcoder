d, n = map(int, input().split())

if d == 0:
    if n == 100:
        print(n+1)
    else:
        print(n)
else:
    if n == 100:
        print(100**d*(n+1))
    else:
        print(100**d*n)