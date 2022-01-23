n = int(input())
a = list(map(int, input().split()))
ans = 0
a.sort(reverse=True)
now = 0
for i in range(n):
    if i == 0:
        continue
    ans += a[now]
    if i%2 == 1:
        now += 1
print(ans)