from itertools import product
n = int(input())
A = []
XY = []
for _ in range(n):
    a = int(input())
    A.append(a)
    l = []
    for _ in range(a):
        x, y = map(int, input().split())
        l.append([x, y])
    XY.append(l)
L = list(product([False, True], repeat=n))
ans = 0
for l in L:
    evi = [0]*n
    for i in range(len(l)):
        if l[i]:
            evi[i] = 1
    cnt = 0
    judge = True
    for i in range(len(l)):
        if l[i]:
            num = A[i]
            for j in range(num):
                if XY[i][j][1] == 1:
                    if evi[XY[i][j][0] - 1] != 1:
                        judge = False
                        break
                else:
                    if evi[XY[i][j][0] - 1] != 0:
                        judge = False
                        break
            if judge:
                cnt += 1
    if judge:
        ans = max(ans, cnt)
print(ans)


    
