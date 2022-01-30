h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = []
for i in range(w):
    l = []
    for j in range(h):
        l.append(a[j][i])
    b.append(l)
for ans in b:
    print(*ans)