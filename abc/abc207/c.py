import bisect

n = int(input())
lr = []
for _ in range(n):
    t, l, r = map(int, input().split())
    if t == 1:
        lr.append([l, r])
    elif t == 2:
        lr.append([l, r-0.1])
    elif t == 3:
        lr.append([l+0.1, r])
    else:
        lr.append([l+0.1, r-0.1])
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        l1 = lr[i][0]
        r1 = lr[i][1]
        l2 = lr[j][0]
        r2 = lr[j][1]
        if r1 < l2 or l1 > r2:
            continue
        ans += 1
print(ans)