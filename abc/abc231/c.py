import bisect
n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]
a.sort()
for i in range(q):
    num = bisect.bisect_left(a, x[i])
    print(n - num)
