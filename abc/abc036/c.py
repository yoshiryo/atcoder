from bisect import bisect_left
n = int(input())
a = [int(input()) for _ in range(n)]
na = list(set(sorted(a)))
ans = []
for i in range(n):
    index = bisect_left(na, a[i])
    ans.append(index)
for i in ans:
    print(i)