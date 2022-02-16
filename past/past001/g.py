from itertools import product, combinations
n = int(input())
L = list(product([1, 2, 3], repeat = n))
A = []
for i in range(n-1):
    a = list(map(int,input().split()))
    a = [0]*(i+1) + a
    A.append(a)
ans = -100000000000
for l in L:
    group = [[] for _ in range(3)]
    for i in range(n):
        index = l[i] - 1
        group[index].append(i)
    all = []
    cnt = 0
    for i in range(len(group)):
        g = group[i]
        pair = combinations(g, 2)
        for x in pair:
            x = list(x)
            p1 = x[0]
            p2 = x[1]
            cnt += A[p1][p2]
    ans = max(ans, cnt)
print(ans)