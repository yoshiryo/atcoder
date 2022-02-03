num = list(map(int, input().split()))
num.sort()
ma = num[-1]
d1 = ma - num[0]
d2 = ma - num[1]
if d1%2 == 0 and d2%2 == 0:
    print(d1//2 + d2//2)
elif d1%2 == 1 and d2%2 == 1:
    d1 -= d2
    print(d1//2 + d2)
else:
    d1 -= d2
    print((d1+1)//2 + d2 + 1)