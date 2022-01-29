from collections import defaultdict
n = int(input())
l = []
ans = 0
for _ in range(n):
    s = sorted(input())
    l.append(''.join(s))
d = defaultdict(int)
for i in range(n):
    s = l[i]
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
x = list(d.values())
for i in range(len(d)):
    a = x[i]
    ans += a*(a-1)/2
print(int(ans))