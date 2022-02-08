n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = sum(a[:k])
ans = cnt
for i in range(k, n):
    cnt -= a[i-k]
    cnt += a[i]
    ans += cnt
print(ans)