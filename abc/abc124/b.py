n = int(input())
h = list(map(int, input().split()))
ans = 1
ma = h[0]
for i in range(1, n):
    if ma <= h[i]:
        ans += 1
        ma = h[i]
print(ans)