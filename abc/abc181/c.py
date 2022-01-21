n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            dx1 = xy[j][0] - xy[i][0]
            dx2 = xy[k][0] - xy[i][0]
            dy1 = xy[j][1] - xy[i][1]
            dy2 = xy[k][1] - xy[i][1]
            if dx2*dy1 == dx1*dy2:
                print("Yes")
                exit()
print("No")