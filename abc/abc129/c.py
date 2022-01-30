n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]
mod = 10**9 + 7

safe = [True]*(n+1)
for i in a:
    safe[i] = False

dp = [0]*(n+1)
dp[0] = 1
for i in range(1, n+1):
    if safe[i]:
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= mod
    else:
        dp[i] = 0
print(dp[n])
