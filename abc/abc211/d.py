import collections

n, m = map(int,input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
mod = 10**9 + 7

que = collections.deque()
dist = [-1] * n
cnt = [0] * n
dist[0] = 0
cnt[0] = 1
que.append(0)

while len(que) != 0:
    p = que.popleft()
    for i in g[p]:
        if dist[i] == -1:
            dist[i] = dist[p] + 1
            que.append(i)
            cnt[i] = cnt[p]
        elif dist[i] == dist[p] + 1:
            cnt[i] += cnt[p]
            cnt[i] %= mod

print(cnt[n-1])