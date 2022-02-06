from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
all = []
alp = "abcdefghijklmnopqrstuvwxyz"
for i in range(n):
    c = Counter(list(s[i]))
    cnt = [0]*26
    for k, val in c.items():
        index = alp.find(k)
        cnt[index] = val
    all.append(cnt)
ans = ""
for i in range(26):
    cnt = 10**10
    for j in range(n):
        cnt = min(cnt, all[j][i])
    ans += alp[i]*cnt
print(ans)