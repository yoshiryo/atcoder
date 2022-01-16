from collections import deque
n, m = map(int, input().split())
g=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
ans = 0
for i in range(n):
    q = deque()
    q.append(i)
    checked = [False]*n
    #checked[i] = True 
    ans += 1
    while q:
        v = q.popleft()
        checked[v] = True
        for u in g[v]:
            if checked[u]:
                continue
            q.append(u)
            checked[u] = True
            ans += 1
print(ans)