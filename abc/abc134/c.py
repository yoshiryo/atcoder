n = int(input())
a = [int(input()) for _ in range(n)]
na = sorted(a, reverse=True)
ma = na[0]
ma2 = na[1]
for i in range(n):
    if ma == a[i]:
        print(ma2)
    else:
        print(ma)
