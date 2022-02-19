n = int(input())
a = list(map(int, input().split()))
mod = 998244353
b = [0]
cnt = 0
for i in range(n):
    cnt += a[i]
    b.append(cnt)
b.sort()
ans = 0
for i in range(n+1):
    ans += (2*i - n)*b[i]
    ans %= mod
print(ans)