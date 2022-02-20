import itertools
a1, a2, a3 = map(int, input().split())
a = [a1, a2, a3]
n = a1 + a2 + a3
all = itertools.permutations(range(1, n+1), n)
ans = 0
for part in all:
    part = list(part)
    a1_l = part[:a1]
    a2_l = part[a1:a1+a2]
    a3_l = part[a1+a2:]
    x = [a1_l, a2_l, a3_l]
    judge = True
    for i in range(3):
        for j in range(1, a[i]):
            if x[i][j] <= x[i][j-1]:
                judge = False
                break
    for i in range(1, 3):
        for j in range(a[i]):
            if x[i][j] <= x[i-1][j]:
                judge = False
                break
    if judge:
        ans += 1
print(ans)    
