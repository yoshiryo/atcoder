n, m = map(int, input().split())
s = [input() for _ in range(n)]
D = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
ans = [[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if s[i][j] == "#":
            cnt = 1
        else:
            cnt = 0
        for d in D:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < n and 0 <= nj < m and s[ni][nj] == "#":
                cnt += 1
        ans[i].append(str(cnt))
for i in ans:
    print("".join(i))