from collections import defaultdict 
n, m = map(int, input().split())
s = list(input().split())
t = list(input().split())
d = defaultdict(int)
for i in range(n):
    d[s[i]] = i
ans = ["No"]*n
for i in range(m):
    ans[d[t[i]]] = "Yes"
for a in ans:
    print(a)