import functools
def euclid(a, b):#ユークリッド（最大公約数(二つ))
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def gcd(nums):#最大公約数(複数)
    return functools.reduce(euclid, nums)

def multiple(a, b):#最小公倍数(2つ)
    return a*b // euclid(a, b) 

def lcm(nums):#最初公倍数(複数)
    return functools.reduce(multiple, nums)

N, X = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
d = []
for i in range(N):
    d.append(abs(X - x[i]))
print(gcd(d))