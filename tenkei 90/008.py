n = int(input())
s = input()
t = "atcoder"
mod = 10**9 + 7
dp = [[0]*(len(t) + 1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0] = 1
for i in range(n):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
            dp[i+1][j+1] %= mod
        else:
            dp[i+1][j+1] = dp[i][j+1]
            dp[i+1][j+1] %= mod
print(dp[n][len(t)])