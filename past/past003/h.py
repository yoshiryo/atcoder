n, l = map(int, input().split())
x = set(list(map(int, input().split())))
t1, t2, t3 = map(int, input().split())
dp = [10**10]*(l+4)
dp[0] = 0
for i in range(l):
    time = dp[i] + t1
    if i+1 in x:
        time += t3
    if dp[i+1] > time:
        dp[i+1] = time

    time = dp[i] + t1 + t2
    if i+2 in x:
        time += t3
    if dp[i+2] > time:
        dp[i+2] = time
    
    time = dp[i] + t1 + 3*t2
    if i+4 in x:
        time += t3
    if dp[i+4] > time:
        dp[i+4] = time

ans = min(dp[l], dp[l-1] + t1//2 + t2//2, dp[l-2] + t1//2 + 3*t2//2, dp[l-3] + t1//2 + 5*t2//2)
print(ans)