n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
ns = list(set(s))
ans = 0
for i in range(len(ns)):
    cnt1 = s.count(ns[i])
    cnt2 = t.count(ns[i])
    d = cnt1 - cnt2
    ans = max(d, ans)
print(ans)