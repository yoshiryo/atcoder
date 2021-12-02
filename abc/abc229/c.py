n, w = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab = sorted(ab, key=lambda x:(x[0]), reverse=True)
ans = 0
for i in range(n):
    a = ab[i][0]
    b = ab[i][1]
    if b >= w:
        ans += a*w
        break
    else:
        ans += a*b
        w -= b
print(ans)