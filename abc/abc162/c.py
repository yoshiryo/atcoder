import functools
def euclid(a, b):#ユークリッド（最大公約数(二つ))
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

k = int(input())
ans = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            ab = euclid(a, b)
            ans += euclid(ab, c)
print(ans)

