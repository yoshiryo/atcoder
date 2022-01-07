n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 1
mod = 10**9 + 7

for i in range(n):
    su = 0
    for j in range(6):
        su += a[i][j]
    ans = ans*su%mod
print(ans)