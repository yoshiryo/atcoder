n = int(input())
if n < 2015:
    print(-1)
elif n < 2017:
    print(n - 2015 + 1)
elif n == 2017:
    print(-1)
else:
    print(n - 2016 + 1)