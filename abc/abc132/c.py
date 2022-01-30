from bisect import bisect_left
n = int(input())
d = list(map(int, input().split()))
d.sort()
mid = n//2
ans = 0
for k in range(1, 10**5 + 1):
    index = bisect_left(d, k)
    if index == mid:
        ans += 1
print(ans)

