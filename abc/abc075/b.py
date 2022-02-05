h, w = map(int, input().split())
s = [input() for _ in range(h)]
D = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
ans = []
for i in range(h):
    part = ""
    for j in range(w):
        if s[i][j] == ".":
            cnt = 0
            for d in D:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < h and 0 <= nj < w:
                    if s[ni][nj] == "#":
                        cnt += 1
            part += str(cnt)
        else:
            part += "#"
    ans.append(part)
for a in ans:
    print(a)