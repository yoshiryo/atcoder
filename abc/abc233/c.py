n, x = map(int, input().split())
l = []
a = []
for _ in range(n):
    L = list(map(int, input().split()))
    l.append(L[0])
    a.append(L[1:])

pro = [1]
for i in range(n):
    tpro = []
    for ai in a[i]:
        for p in pro:
            tpro.append(ai*p)
    pro = tpro
ans = pro.count(x)
print(ans)