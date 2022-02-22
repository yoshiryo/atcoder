n, k = map(int, input().split())
a = list(map(int, input().split()))
match = []
for i in range(n):
    if a[i] < k:
        match.append([a[i], i+1])
match = sorted(match, key=lambda x:x[0])
if len(match) == 0:
    print(-1)
else:
    print(match[-1][1])