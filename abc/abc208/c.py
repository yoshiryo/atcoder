n, k = map(int, input().split())
a = list(map(int, input().split()))
na = []
for i in range(n):
    na.append([a[i], i])
na = sorted(na, key=lambda x:x[0])
cnt = k//n
ans = [cnt]*n
k -= cnt*n

for i in range(n):
    if k == 0:
        break
    k -= 1
    ans[na[i][1]] += 1
for i in ans:
    print(i)
