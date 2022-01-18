from itertools import product

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(int, input().split())) for _ in range(k)]
L = list(product([False, True], repeat=k))
ma = 0
for l in L:
    boal = [0]*n
    cnt = 0
    for i in range(k):
        if l[i] == True:
            boal[cd[i][0]-1] = 1
        else:
            boal[cd[i][1]-1] = 1
    for i in range(m):
        if boal[ab[i][0]-1] == 1 and boal[ab[i][1]-1] == 1:
            cnt += 1
    ma = max(ma, cnt)
print(ma)