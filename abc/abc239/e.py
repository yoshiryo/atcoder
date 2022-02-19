from collections import deque
n, Q = map(int, input().split())
x = list(map(int, input().split()))
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    ma = max(a, b)
    mi = min(a, b)
    g[mi].append(ma)
all = []
for i in range(n):
    q = deque()
    q.append(i+1)
    checked = [False]*(n+1)
    l = []
    while q:
        v = q.pop()
        checked[v] = True 
        l.append(x[v-1])
        for u in g[v]:
            if checked[u]:
                continue
            q.append(u)
    all.append(l)
nall = []
for i in range(len(all)):
    l = sorted(all[i], reverse=True)
    nall.append(l)
for _ in range(Q):
    v, k = map(int, input().split())
    print(nall[v-1][k-1])