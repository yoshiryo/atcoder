n, m, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
c = list(map(int, input().split()))
for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        x = s[1]
        x -= 1
        color = c[x]
        print(color)
        l = g[x]
        for i in range(len(l)):
            c[l[i]] = color
    else:
        x, y = s[1:]
        x -= 1
        color = c[x]
        print(color)
        c[x] = y