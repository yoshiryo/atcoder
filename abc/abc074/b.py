n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += min(x[i], abs(x[i] - k))*2
print(ans)