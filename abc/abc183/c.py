import itertools
n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
all = itertools.permutations(range(1, n), n-1)
ans = 0
for a in all:
    time = 0
    now = 0
    for city in a:
        time += t[now][city]
        now = city
    time += t[now][0]
    if time == k:
        ans += 1
print(ans)