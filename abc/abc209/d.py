from collections import deque

n, Q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
q = deque([(1, 0)])
checked = [-1]*(n+1)
while q:
    np, dep = q.popleft()
    if checked[np] != -1:
        continue
    checked[np] = dep

    for u in g[np]:
        if checked[u] != -1:
            continue
        q.append((u, dep + 1))
ans = []
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if abs(checked[c] - checked[d]) % 2:
        ans.append("Road")
    else:
        ans.append("Town")
for a in ans:
    print(a)