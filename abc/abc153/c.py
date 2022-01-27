n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse=True)
ans = 0
for i in range(n):
    if k <= 0:
        ans += h[i]
    else:
        k -= 1
print(ans)