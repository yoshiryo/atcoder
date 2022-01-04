from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))
a_cum = [0]*(n+1)
for i in range(n):
    a_cum[i+1] = a_cum[i] + a[i]

d = defaultdict(int)
ans = 0

for i in range(1, n+1):
    d[a_cum[i-1]] += 1
    ans += d[a_cum[i] - k]
print(ans)