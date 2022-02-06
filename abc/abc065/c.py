n, m = map(int, input().split())
mod = 10**9 + 7
if abs(n-m) >= 2:
    print(0)
else:
    cnt_n = 1
    cnt_m = 1
    for i in range(1, n+1):
        cnt_n = (cnt_n*i)%mod
    for i in range(1, m+1):
        cnt_m = (cnt_m*i)%mod
    if abs(n-m) == 1:
        print(cnt_n*cnt_m%mod)
    else:
        print(2*cnt_n*cnt_m%mod)

