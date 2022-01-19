n, m, t = map(int, input().split())
ma = n
ab = [list(map(int, input().split())) for _ in range(m)]
now = 0
for i in range(m):
    a, b = ab[i]
    if a - now >= n:
        print("No")
        exit()
    else:
        n -= a - now
        n = min(ma, n + b - a)
        now = b
if t - now >= n:
    print("No")
else:
    print("Yes")