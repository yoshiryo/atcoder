import bisect
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 10**9

for i in range(n):
    l = bisect.bisect_left(b, a[i])
    r = l - 1
    if r < 0:
        lnum = abs(a[i] - b[l])
        rnum = 10**9
    elif l >= m:
        lnum = 10**9
        rnum = abs(a[i] - b[r])
    else:
        lnum = abs(a[i] - b[l])
        rnum = abs(a[i] - b[r])
    ans = min(ans, lnum, rnum)

print(ans)
