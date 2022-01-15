import collections
n, q = map(int, input().split())
a = list(map(int, input().split()))
d = collections.defaultdict(list)
for i in range(n):
    d[a[i]].append(i+1)
for _ in range(q):
    x, k = map(int, input().split())
    if len(d[x]) < k:
        print(-1)
    else:
        print(d[x][k-1])
