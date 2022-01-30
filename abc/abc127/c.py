n, m = map(int, input().split())
L = []
R = []
for _ in range(m):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
mi = max(L)
ma = min(R)
if ma - mi + 1 <= 0:
    print(0)
else:
    print(ma - mi + 1)
