n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in range(n-m+1):
    for j in range(n-m+1):
        cnt = 0
        for k in range(m):
            for l in range(m):
                if a[i+k][j+l] == b[k][l]:
                    cnt += 1
        if cnt == m*m:
            print("Yes")
            exit()
print("No")