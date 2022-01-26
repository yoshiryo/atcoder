n, m = map(int, input().split())
sc = []
ma = 0
for _ in range(m):
    s, c = map(int, input().split())
    sc.append([s, c])
    ma = max(ma, s)
ma = max(ma, n)
for i in range(1000):
    num = str(i)
    if len(num) < ma:
        continue
    judge = True
    for s, c in sc:
        if num[s-1] != str(c):
            judge = False
            break
    if judge:
        print(i)
        exit()
print(-1)
