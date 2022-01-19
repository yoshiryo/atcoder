n = int(input())
dp = [0]*(n+1)
dp[0] = 1
for i in range(n):
    s = input()
    if s == "AND":
        dp[i+1] = dp[i]
    else:
        dp[i+1] = dp[i] + 2**(i+1)
print(dp[n])