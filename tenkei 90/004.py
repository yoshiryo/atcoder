h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
w_sum = []
h_sum = []
for i in range(h):
    sum = 0
    for j in range(w):
        sum += a[i][j]
    w_sum.append(sum)

for i in range(w):
    sum = 0
    for j in range(h):
        sum += a[j][i]
    h_sum.append(sum)
ans = []
for i in range(h):
    l = []
    for j in range(w):
        l.append(w_sum[i] + h_sum[j] - a[i][j])
    ans.append(l)
for i in range(h):
    print(*ans[i])