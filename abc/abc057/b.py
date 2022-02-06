n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]
ans = []
for i in range(n):
    a, b = ab[i]
    cnt = []
    for j in range(m):
        c, d = cd[j]
        diff = abs(a - c) + abs(b - d)
        cnt.append([diff, j+1])
    cnt = sorted(cnt, key=lambda x:(x[0], x[1]))
    ans.append(cnt[0][1])
for i in ans:
    print(i)