import bisect
n = int(input())
a = list(map(int, input().split()))
q = int(int(input()))
a.sort()
for i in range(q):
    b = int(input())
    t1 = int(1e9)
    t2 = int(1e9)
    r_index = bisect.bisect_left(a, b)
    l_index = r_index - 1
    if r_index >= 1:
        t1 = abs(a[l_index] - b)
    if r_index < n:
        t2 = abs(a[r_index] - b)
    ans = min(t1, t2)
    print(ans)