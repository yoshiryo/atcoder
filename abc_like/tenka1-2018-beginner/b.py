a, b, k = map(int, input().split())
now = "taka"
for _ in range(k):
    if now == "taka":
        if a%2 == 1:
            a -= 1
        b += a//2
        a //= 2
        now = "aoki"
    else:
        if b%2 == 1:
            b -= 1
        a += b//2
        b //= 2
        now = "taka"
print(a, b)