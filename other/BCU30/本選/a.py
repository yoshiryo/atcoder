n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
ans = sum(a[:k])
for i in range(k, n):
    ans += a[i]*2
print(ans)