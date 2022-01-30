import functools

def euclid(a, b):#ユークリッド（最大公約数(二つ))
    if b == 0:
        return a
    else:
        return euclid(b, a%b)
def multiple(a, b):#最小公倍数(2つ)
    return a*b // euclid(a, b) 
a, b, c, d = map(int, input().split())

c_cnt = b//c - (a-1)//c
d_cnt = b//d - (a-1)//d
eu = multiple(c, d)
cd_cnt = b//eu - (a-1)//eu
print((b-a+1) - (c_cnt+d_cnt-cd_cnt))