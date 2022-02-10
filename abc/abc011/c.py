N = int(input())
NG = [int(input()) for _ in range(3)]
f_inf = float('inf')
dp = [f_inf] * 301
dp[N] = 0
for i in range(N, -1, -1):
    if i in NG:
        continue
    for j in range(1, 4):
        dp[i-j] = min(dp[i]+1, dp[i-j])
if dp[0] <= 100:
    print('YES')
else:
    print('NO')
        