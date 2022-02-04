from collections import Counter
n = int(input())
a = list(input().split())
c = Counter(a)
key = list(c.keys())
ans = 0
for k in key:
    num = int(k)
    if c[k] >= num:
        ans += c[k] - num
    else:
        ans += c[k]
print(ans)