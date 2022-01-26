n, A, B = map(int, input().split())
mod = 10**9 + 7
s = pow(2, n, mod) - 1

def fur(n,r):
    p,q = 1,1
    for i in range(r):
        p = p*(n-i)%mod
        q = q*(i+1)%mod
    return p * pow(q,mod-2,mod) % mod

print((s - fur(n, A) - fur(n, B))%mod)