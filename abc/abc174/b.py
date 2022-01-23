n, d = map(int, input().split())
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    dis = (x**2 + y**2)**0.5
    if dis <= d:
        ans += 1
print(ans)