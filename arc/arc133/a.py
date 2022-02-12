n = int(input())
a = list(map(int, input().split()))
a = a + [0]
for i in range(n):
    if a[i] > a[i + 1]:
        delete = a[i]
        break
ans = []
for i in range(n):
    if a[i] != delete:
        ans.append(a[i])
print(*ans)