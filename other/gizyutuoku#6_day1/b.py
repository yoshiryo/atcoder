from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = len(set(a))
c = Counter(a)
cnt = 0
for _, val in c.most_common():
    if val >= 2:
        cnt += val - 1
if cnt >= m:
    ans += m
else:
    ans += cnt
print(ans)