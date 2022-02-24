def euclid(a, b):#ユークリッド（最大公約数(二つ))
    if b == 0:
        return a
    else:
        return euclid(b, a%b)
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(euclid(a, b))
