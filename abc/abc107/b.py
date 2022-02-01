h, w = map(int, input().split())
a = [input() for _ in range(h)]
na = []
for i in range(h):
    judge = True
    for j in range(w):
        if a[i][j] == "#":
            judge = False
            break
    if not judge:
        na.append(a[i])
ans = []
w = len(na[0])
h = len(na)
for i in range(w):
    ns = ""
    judge = True
    for j in range(h):
        ns += na[j][i]
        if na[j][i] == "#":
            judge = False
    if not judge:
        ans.append(ns)
w = len(ans)
h = len(ans[0])
for i in range(h):
    s = ""
    for j in range(w):
        s += ans[j][i]
    print(s)