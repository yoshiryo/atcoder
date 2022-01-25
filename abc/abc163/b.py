n, m = map(int, input().split())
a = list(map(int, input().split()))
all = sum(a)
if all > n:
    print(-1)
else:
    print(n - all)