n, k, a = map(int, input().split())
r = (a+k-1)%n
if r == 0:
    print(n)
else:
    print(r)