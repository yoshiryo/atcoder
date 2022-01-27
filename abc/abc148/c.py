def euclid(a, b):#ユークリッド（最大公約数(二つ))
    if b == 0:
        return a
    else:
        return euclid(b, a%b)
def multiple(a, b):#最小公倍数(2つ)
    return a*b // euclid(a, b) 
a, b = map(int, input().split())
print(multiple(a, b))

