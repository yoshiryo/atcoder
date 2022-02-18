from collections import deque
n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]
D = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 0
for i in range(n):
    for j in range(m):
        if s[i][j] == "#":
            s[i][j] = "."
            cnt = [[-1]*m for _ in range(n)]
            q = deque()
            q.append((i, j))
            cnt[i][j] = 0
            while q:
                y, x = q.pop()
                for d in D:
                    ni = y + d[0]
                    nj = x + d[1]
                    if 0 <= ni < n and 0 <= nj < m and s[ni][nj] == "." and cnt[ni][nj] == -1:
                        cnt[ni][nj] = 0
                        q.append((ni, nj))
            judge = True
            for ni in range(n):
                for nj in range(m):
                    if s[ni][nj] == "." and cnt[ni][nj] == -1:
                        judge = False
                        break
            if judge:
                ans += 1
            s[i][j] = "#"
print(ans)