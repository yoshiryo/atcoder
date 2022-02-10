n, m = map(int, input().split())
mat = [[10000 for _ in range(n)] for _ in range(n)]

for i in range(n):
	mat[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    mat[a-1][b-1] = mat[b-1][a-1] = 1

for i in range(n):
	for x in range(n):
		for y in range(n):
			mat[x][y] = min(mat[x][y], mat[x][i]+mat[i][y])

for i in range(n):
    cnt = 0
    for x in range(n):
        if mat[i][x] == 2:
            cnt += 1
    print(cnt)