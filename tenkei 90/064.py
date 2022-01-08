n, q = map(int, input().split())
a = list(map(int, input().split()))
b = []
ans = 0
for i in range(n-1):
    b.append(a[i+1]-a[i])
    ans += abs(b[i])

for _ in range(q):
    l, r, v = map(int, input().split())
    if l != 1:
        ans -= abs(b[l-2])
        b[l-2] += v
        ans += abs(b[l-2])
    if r != n:
        ans -= abs(b[r-1])
        b[r-1] -= v
        ans += abs(b[r-1])
    print(ans)