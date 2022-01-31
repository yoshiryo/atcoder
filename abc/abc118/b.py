n, m = map(int, input().split())
ans = [0]*m
for _ in range(n):
    ka = list(map(int, input().split()))
    k = ka[0]
    a = ka[1:]
    for i in range(k):
        ans[a[i]-1] += 1
print(ans.count(n))