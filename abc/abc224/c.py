n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x1 = xy[i][0]
            y1 = xy[i][1]
            x2 = xy[j][0]
            y2 = xy[j][1]
            x3 = xy[k][0]
            y3 = xy[k][1]

            s = abs((x1-x3)*(y2-y3) - (x2-x3)*(y1-y3)) / 2
            if s != 0:
                ans += 1
print(ans)