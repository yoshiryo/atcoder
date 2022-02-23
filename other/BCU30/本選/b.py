n = int(input())
A = list(map(int, input().split())) + [0]
ans = 0
for i in range(n):
    if A[i] > A[i + 1]:
        ans += 1
print(ans)
