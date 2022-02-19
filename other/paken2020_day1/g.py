from itertools import product
n, m = map(int, input().split())
lrx = [list(map(int, input().split())) for _ in range(m)]
L = list(product([False, True], repeat=n))
ans = -1
for l in L:
    judge = []
    for i in range(n):
        if l[i]:
            judge.append(1)
        else:
            judge.append(0)
    p = True
    for i in range(m):
        left, right, x = lrx[i]
        left -= 1
        cnt = judge[left:right].count(1)
        if x != cnt:
            p = False
            break
    if p:
        ans = max(ans, judge.count(1))
print(ans)
    