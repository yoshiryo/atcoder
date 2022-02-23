a, b, t = map(int, input().split())
d = b - a
next = b + d
for _ in range(10**6):
    if next >= t:
        print(next)
        exit()
    next += d
