a, b, c = map(int, input().split())
mod = 10**9 + 7
a %= mod
b %= mod
c %= mod
print(a*b*c%mod)