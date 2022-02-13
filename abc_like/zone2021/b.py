n, d, h = map(int, input().split())
dh = [list(map(int, input().split())) for _ in range(n)]
a = 10**10
for i in range(n):
    dx = d - dh[i][0]
    dy = h - dh[i][1]
    b = dy/dx
    a = min(a, b)
ans = h - a*d
print(max(ans, 0)) 