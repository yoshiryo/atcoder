h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
D = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(h):
    for j in range(w):
        if c[i][j] == ".":
            allow = ["1", "2", "3", "4", "5"]
            for d in D:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < h and 0 <= nj < w:
                    if c[ni][nj] in allow:
                        allow.remove(c[ni][nj])
            c[i][j] = allow[0]
for i in c:
    print("".join(i))