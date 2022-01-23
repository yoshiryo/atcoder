n = int(input())
a = list(map(int, input().split()))
all = 0
for i in range(n):
    all ^= a[i]
ans = []
for i in range(n):
    ans.append(all ^ a[i])
print(*ans)