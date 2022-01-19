n, m = map(int, input().split())
a = list(map(int, input().split()))
if m == 0:
    ans = 1
else:
    C = []
    a.sort()
    if a[0] - 1 != 0:
        mi = a[0] - 1
        C.append(a[0] - 1)
    else:
        mi = 10**9
    for i in range(1, m):
        diff = a[i] - a[i-1] - 1
        if diff != 0:
            mi = min(mi, diff)
            C.append(diff)
    diff = n - a[m-1]
    if diff != 0:
        mi = min(mi, diff)
        C.append(diff)
    ans = 0
    for i in range(len(C)):
        if C[i]%mi == 0:
            ans += C[i]//mi
        else:
            ans += C[i]//mi
            ans += 1
print(ans)