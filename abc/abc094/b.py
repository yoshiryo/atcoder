from bisect import bisect_left, bisect_right
n, m, x = map(int, input().split())
a = list(map(int, input().split()))
index1 = bisect_right(a, x)
index2 = bisect_left(a, x)
ans = min(len(a[:index1]), len(a[index2:]))
print(ans)
