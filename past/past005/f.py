from itertools import product
n, m = map(int, input().split())
all = []
for _ in range(m):
    a, b, c = map(int, input().split())
    all.append([a, b, c])
L = list(product([False, True], repeat=n))
ans = 0
for l in L:
    num = []
    for i in range(n):
        if l[i]:
            num.append(i+1)
    cnt1 = set()
    for j in range(m):
        cnt2 = 0
        t = []
        for k in range(3):
            if all[j][k] in num:
                cnt2 += 1
            else:
                t.append(all[j][k])
        if cnt2 == 2:
            cnt1.add(t[0])
    ans = max(ans, len(cnt1))
print(ans)