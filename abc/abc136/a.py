a, b, c = map(int, input().split())
rem = a - b
if rem >= c:
    print(0)
else:
    print(c - rem)