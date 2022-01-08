import bisect
n, m = map(int, input().split())
ab = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ab[a].append(b)
    ab[b].append(a)
ans = 0
for i in range(n):
    ab[i].sort()
    index = bisect.bisect_left(ab[i], i)
    if index == 1:
        ans += 1
print(ans)