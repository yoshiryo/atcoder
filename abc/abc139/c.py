n = int(input())
h = list(map(int, input().split()))
ans = 0
now = h[0]
cnt = 0
for i in range(1, n):
    if now >= h[i]:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
    now = h[i]
ans = max(ans, cnt)
print(ans)