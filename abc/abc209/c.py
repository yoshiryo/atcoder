n = int(input())
c = list(map(int, input().split()))
c.sort()
ans = 1
mod = 10**9 + 7
for i in range(n):
    ans = ans * max(0, c[i] - i) % mod
print(ans)