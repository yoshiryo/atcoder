from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
c = Counter(s)
ma = 0
for val in c.values():
    ma = max(ma, val)
ans = []
for k, val in c.items():
    if ma == val:
        ans.append(k)
ans.sort()
for a in ans:
    print(a)
