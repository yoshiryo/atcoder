from collections import deque

n = int(input())
t = [0]*(n+1)
g = [[] for _ in range(n + 1)]
ans = 0
for i in range(1, n+1):
    t[i], k, *a = map(int, input().split())
    for j in range(k):
        g[i].append(a[j])

seen = [False]*(n+1)
q = deque()
q.append(n)
seen[n] = True

while q:
    v = q.pop()
    ans += t[v]
    for u in g[v]:
        if seen[u]:
            continue
        q.append(u)
        seen[u] = True 
print(ans)