n, m = map(int, input().split())
for a in range(n+1):
    c = (m - a*2) - 3*(n - a)
    b = n - a - c
    if b >= 0 and c >= 0:
        print(a, b, c)
        exit()
print(-1, -1, -1)