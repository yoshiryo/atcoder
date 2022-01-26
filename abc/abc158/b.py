n, a, b = map(int, input().split())
ab = a + b
cnt = n//ab
ans = cnt*a
n -= cnt*ab
if n > a:
    print(ans + a)
else:
    print(ans + n)