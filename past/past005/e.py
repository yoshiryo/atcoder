H,W = map(int,input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]
A = [[] for _ in range(4)]
for h in range(H):
    for w in range(W):
        if T[h][w] == '#':
            A[0].append((h,w))
            A[1].append((w,H-h))
            A[2].append((H-h,W-w))
            A[3].append((W-w,h))
m = max(H,W)
for h in range(-m,m):
    for w in range(-m,m):
        for a in A:
            f = True
            for p in a:
                x = p[0] - h
                y = p[1] - w
                if x < 0 or H <= x or y < 0 or W <= y or S[x][y] == '#':
                    f = False
                    break
            if f:
                print('Yes')
                exit()
print('No')
