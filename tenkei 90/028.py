n = int(input())
cnt = [[0] * 1001 for _ in range(1001)]
for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    cnt[lx][ly] += 1
    cnt[lx][ry] -= 1
    cnt[rx][ly] -= 1
    cnt[rx][ry] += 1

for i in range(1, 1001):
    for j in range(1001):
        cnt[i][j] += cnt[i-1][j]

for i in range(1001):
    for j in range(1, 1001):
        cnt[i][j] += cnt[i][j-1]

ans = [0] * (n + 1)
for i in range(1001):
    for j in range(1001):
        ans[cnt[i][j]] += 1
for i in range(1, n+1):
    print(ans[i])

