from itertools import product
n, m, x = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]
L = list(product([False, True], repeat=n))
ans = 10**10
for l in L:
    money = 0
    algo = [0]*m
    for i in range(n):
        if l[i]:
            money += c[i][0]
            for j in range(m):
                algo[j] += c[i][j+1]
    if min(algo) >= x:
        ans = min(ans, money)
if ans == 10**10:
    print(-1)
else:
    print(ans)
