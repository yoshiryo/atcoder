from bisect import bisect_right
n = int(input())
a = list(map(int, input().split()))
ok = [1, 3, 7, 9]
ans = 0
for i in range(n):
    index = bisect_right(ok, a[i]) - 1
    ans += a[i] - ok[index]
print(ans)