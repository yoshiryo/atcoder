n = int(input())
a = list(map(int, input().split()))
x = 0
y = sum(a)
ans = 10**10
for i in range(n-1):
    x += a[i]
    y -= a[i]
    diff = abs(x - y)
    ans = min(ans, diff)
print(ans)