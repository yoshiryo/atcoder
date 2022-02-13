h, w = map(int, input().split())
s = [input() for _ in range(h)]
D = [[-1, 0], [1, 0], [0, -1], [0, 1]]
cnt = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            for d in D:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < h and 0 <= nj < w:
                    if s[ni][nj] == ".":
                        cnt += 1
print(cnt//2)