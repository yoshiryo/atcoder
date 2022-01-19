n = int(input())
a = list(map(int, input().split()))
ans = 0
for l in range(n):
    mi = 10**5 + 1
    for r in range(l, n):
        d = r - l + 1
        mi = min(mi, a[r])
        all = d*mi
        ans = max(ans, all)
print(ans)