n, k = map(int, input().split())
ans = n
if n%k == 0:
    print(0)
else:
    cnt1 = n//k
    cnt2 = cnt1 + 1
    ans = min(abs(n - cnt1*k), abs(n - cnt2*k))
    print(ans)