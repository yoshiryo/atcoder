a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
ans = [[0]*3 for _ in range(3)]
for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                ans[i][j] = 1
for i in range(3):
    if ans[i][0] + ans[i][1] + ans[i][2] == 3:
        print("Yes")
        exit()
for i in range(3):
    if ans[0][i] + ans[1][i] + ans[2][i] == 3:
        print("Yes")
        exit()
if ans[0][0] + ans[1][1] + ans[2][2] == 3 or ans[0][2] + ans[1][1] + ans[2][0] == 3:
    print("Yes")
    exit()
print("No")