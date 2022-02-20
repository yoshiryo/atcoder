n = int(input())
s = [list(input()) for _ in range(5)]
dp = [[0]*3 for _ in range(n+1)]
for i in range(n):
    r = 0
    b = 0
    w = 0
    for j in range(5):
        if s[j][i] == "R":
            r += 1
        if s[j][i] == "B":
            b += 1
        if s[j][i] == "W":
            w += 1
    r_cnt = 5 - r
    b_cnt = 5 - b
    w_cnt = 5 - w
    dp[i+1][0] = r_cnt + min(dp[i][1], dp[i][2])
    dp[i+1][1] = b_cnt + min(dp[i][0], dp[i][2])
    dp[i+1][2] = w_cnt + min(dp[i][0], dp[i][1])
print(min(dp[n][0], dp[n][1], dp[n][2]))