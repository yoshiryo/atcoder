a, b, c, k = map(int, input().split())
if a >= k:
    print(k)
else:
    ans = a
    k -= a
    if b >= k:
        print(ans)
    else:
        k -= b
        print(ans - k)