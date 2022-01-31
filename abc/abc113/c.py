n, m = map(int, input().split())
a = []
for i in range(m):
    p, y = map(int, input().split())
    l = [p, y, i]
    a.append(l)

a = sorted(a, key=lambda x:(x[0], x[1]))
ans = []
n = a[0][0]
cnt = 0
for i in range(m):
    if n == a[i][0]:
        cnt += 1
        nl = [a[i][2], a[i][0], cnt]
        ans.append(nl)
    else:
        n = a[i][0]
        cnt = 1
        nl = [a[i][2], a[i][0], cnt]
        ans.append(nl)
ans = sorted(ans, key=lambda x:x[0])

for i in range(len(ans)):
    year = str(ans[i][1])
    num = str(ans[i][2])
    print(year.zfill(6) + num.zfill(6))