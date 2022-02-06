n, m = map(int, input().split())
if 2*n <= m:
    ans = n
    m -= 2*n
    print(ans + m//4)
else:
    print(m//2)
