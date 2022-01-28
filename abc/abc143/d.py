from bisect import bisect_left
n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        p = bisect_left(l, l[i] + l[j])
        ans += p - j - 1
print(ans)