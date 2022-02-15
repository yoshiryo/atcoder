n = int(input())
A = list(map(int,input().split()))
MOD = 10**9 + 7

dp = [[0] * 2 for _ in range(n)]
dp[0][0] = 1
for i in range(n-1):
    dp[i + 1][0] += (dp[i][0] + dp[i][1]) % MOD
    dp[i + 1][1] += dp[i][0] % MOD

ans = A[0]*(dp[-1][0] + dp[-1][1])
for i in range(1, n):
    ans += A[i] * (dp[i][0]*dp[-i][0] - dp[i][1]*dp[-i][1])
print(ans % MOD)