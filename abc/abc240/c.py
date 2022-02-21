n, x = map(int, input().split())
dp = [[False]*(10**4+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(n):
    a, b = map(int, input().split())
    for j in range(10**4+1):
        if dp[i][j-a] and j - a >= 0:
            dp[i+1][j] = True
        if dp[i][j-b] and j - b >= 0:
            dp[i+1][j] = True
if dp[n][x]:
    print("Yes")
else:
    print("No")