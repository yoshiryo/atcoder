n = int(input())
a = list(map(int, input().split()))
a.sort()
s = a[0]
ans = 0
for i in range(1,n):
    ans += a[i]*i-s
    s += a[i]
print(ans)