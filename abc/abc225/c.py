n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
 
for i in range(n):
    for j in range(m):
        if j != m-1:
            if b[i][j] % 7 == 0:
                print("No")
                exit()
for i in range(n):
    for j in range(m-1):
        if b[i][j] + 1 != b[i][j+1]:
            print("No")
            exit()
for i in range(n-1):
    for j in range(m):
            if b[i][j] + 7 != b[i+1][j]: 
                print("No")
                exit()
print("Yes")