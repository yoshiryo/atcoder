n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    if b[i] <= a[i]:
        ans += b[i]
    else:
        ans += a[i]
        re = b[i] - a[i]
        ans += min(a[i+1], re)
        a[i+1] = max(0, a[i+1] - re)
print(ans)