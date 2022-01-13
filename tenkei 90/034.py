from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = defaultdict(int)
l = 0
ans = 0
for r in range(n):
    cnt[a[r]] += 1
    while len(cnt) > k:
        cnt[a[l]] -= 1
        if cnt[a[l]] == 0:
            del cnt[a[l]]
        l += 1
    ans = max(ans, r - l + 1)
print(ans)
