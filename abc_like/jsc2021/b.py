n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
for i in range(n):
    if a[i] not in b:
        ans.append(a[i])
for i in range(m):
    if b[i] not in a:
        ans.append(b[i])
ans.sort()
print(*ans)