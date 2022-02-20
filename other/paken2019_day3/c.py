import itertools
n, m = map(int, input().split())
all = itertools.combinations(range(m), 2)
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for part in all:
    s1 = part[0]
    s2 = part[1]
    cnt = 0
    for i in range(n):
        cnt += max(a[i][s1], a[i][s2])
    ans = max(ans, cnt)
print(ans)