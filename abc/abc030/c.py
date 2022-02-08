import bisect
n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
t = 0
ans = 0
while True:
    id = bisect.bisect_left(a, t)
    if id >= n:
        break
    t = a[id] + x
    id = bisect.bisect_left(b, t)
    if id >= m:
        break
    t = b[id] + y
    ans += 1
print(ans)