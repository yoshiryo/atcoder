n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
all = sum(a)
ans = 0
for i in range(n):
    all -= a[i]
    ans += a[i]*all
print(ans%mod)