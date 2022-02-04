n, y = map(int, input().split())
for i in range(n+1):
    for j in range(n+1):
        k = n - (i + j)
        su = i*10000 + j*5000 + 1000*k
        if k >= 0 and su == y:
            print(i, j, k)
            exit()
print(-1, -1, -1)