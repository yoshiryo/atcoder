n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        dx = (xy[i][0] - xy[j][0]) ** 2
        dy = (xy[i][1] - xy[j][1]) ** 2
        dis = (dx + dy) ** 0.5
        ans = max(ans, dis)
print(ans)