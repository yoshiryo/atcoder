n, k, x = map(int, input().split())
a = list(map(int, input().split()))
all = sum(a)
cnt = 0
for i in range(n):
    if a[i]//x > 0:
        cnt += a[i]//x
        a[i] -= a[i]//x*x
a.sort(reverse=True)
if cnt >= k:
    print(all - k*x)
else:
    all -= cnt*x
    k -= cnt
    if k >= n:
        print(0)
    else:
        for i in range(k):
            all -= a[i]
        print(all)