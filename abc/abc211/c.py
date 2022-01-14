s = input()
t = "chokudai"
dp = [[0]*9 for _ in range(len(s) + 1)]
mod = 10**9 + 7
for i in range(len(s) + 1):
    dp[i][0] = 1
for i in range(1, len(s) + 1):
    for j in range(1, 9):
        if s[i-1] != t[j-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp[len(s)][8])
