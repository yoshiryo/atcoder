def Pow(a,b):
    res = 1
    while b != 0:
        if b % 2 == 1:
            res = res * a % mod
        a = a * a % mod
        b = b // 2
    return res

n, k = map(int, input().split())
mod = 10**9 + 7
if k == 1:
    if n == 1:
        print(1)
    else:
        print(0)
elif n == 1:
    print(k%mod)
elif n == 2:
    print(k*(k-1)%mod)
else:
    print(k*(k-1)%mod*Pow(k-2, n-2)%mod)