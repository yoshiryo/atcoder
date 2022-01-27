n, m = map(int, input().split())
good = [0]*n
bad = [0]*n
for _ in range(m):
    p, s = input().split()
    p = int(p)
    if good[p-1] == 0:
        if s == "WA":
            bad[p-1] += 1
        else:
            good[p-1] = 1
ans = 0
for i in range(n):
    if good[i] == 1:
        ans += bad[i]
print(sum(good), ans)