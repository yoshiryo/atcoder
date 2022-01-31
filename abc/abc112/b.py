n, T = map(int, input().split())
ans = 10**10
for _ in range(n):
    c, t = map(int, input().split())
    if T >= t:
        ans = min(ans, c)
if ans == 10**10:
    print("TLE")
else:
    print(ans)