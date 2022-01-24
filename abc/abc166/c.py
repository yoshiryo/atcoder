n, m = map(int, input().split())
h = list(map(int, input().split()))
ab = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    ab[a].append(b)
    ab[b].append(a)
ans = 0
for i in range(1, n+1):
    judge = True
    now_h = h[i-1]
    for j in ab[i]:
        if h[j-1] >= now_h:
            judge = False
            break
    if judge:
        ans += 1
print(ans)
