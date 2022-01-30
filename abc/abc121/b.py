n, m, c = map(int, input().split())
b = list(map(int, input().split()))
ans = 0
for _ in range(n):
    a = list(map(int, input().split()))
    cnt = c
    for i in range(m):
        cnt += a[i]*b[i]
    if cnt > 0:
        ans += 1
print(ans)