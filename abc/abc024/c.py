n, d, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(d)]
st = [list(map(int, input().split())) for _ in range(k)]
ans = [0]*k
judge = [True]*k
day = 0
for l, r in lr:
    day += 1
    for i in range(k):
        s = st[i][0]
        t = st[i][1]
        if l <= s <= r:
            if l <= t <= r and judge[i]:
                ans[i] = day
                judge[i] = False
            else:
                if s <= t:
                    st[i][0] = r
                else:
                    st[i][0] = l
for i in ans:
    print(i)