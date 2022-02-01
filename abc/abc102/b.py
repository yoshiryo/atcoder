n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        diff = abs(a[i] - a[j])
        ans = max(ans, diff)
print(ans)