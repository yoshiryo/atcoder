import itertools

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
xy = [[0] * n for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    xy[x-1][y-1] = 1
    xy[y-1][x-1] = 1

L = list(itertools.permutations(range(n)))
ans = int(1e9)
for i in range(len(L)):
    p = True
    l = L[i]
    t = 0
    for j in range(n):
        if j < n-1:
            if xy[l[j]][l[j+1]] == 1:
                p = False
                break
        t += a[l[j]][j]
    if p:
        ans = min(ans, t)
if ans == int(1e9):
    print(-1)
else:
    print(ans)