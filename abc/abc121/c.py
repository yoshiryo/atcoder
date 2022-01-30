n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab = sorted(ab, key=lambda x:x[0])
ans = 0
for i in range(n):
    a, b = ab[i]
    if m <= b:
        ans += a*m
        break
    ans += a*b
    m -= b
print(ans)