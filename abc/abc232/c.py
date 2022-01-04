from itertools import permutations

n, m = map(int, input().split())
ab = [[False]*n for _ in range(n)]
cd = [[False]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ab[a][b] = True
    ab[b][a] = True
for _ in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    cd[c][d] = True
    cd[d][c] = True
P = permutations(range(n))
for p in P:
    now = True
    for i in range(n):
        for j in range(n):
            if ab[p[i]][p[j]] != cd[i][j]:
                now = False
    if now:
        print("Yes")
        exit()
print("No")
