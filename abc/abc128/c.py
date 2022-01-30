from itertools import product

n, m = map(int, input().split())
ks = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
l = list(product([False, True], repeat=n))
ans = 0
for light in l:
    judge = []
    for i in range(m):
        cnt = 0
        for j in range(ks[i][0]):
            if light[ks[i][j+1]-1]:
                cnt += 1
        judge.append(cnt%2)
    if judge == p:
        ans += 1
print(ans)