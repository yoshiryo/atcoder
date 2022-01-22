n = int(input())
mod = 10**9 + 7
if n == 1:
    print(0)
else:
    all = (10**n) % mod
    a = 2*9**n % mod
    b = 8**n % mod
    print((all - (a - b))%mod)