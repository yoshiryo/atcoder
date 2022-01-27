n = int(input())
a = list(map(int, input().split()))
now = 1
ans = 0
for i in range(n):
    if a[i] == now:
        now += 1
    else:
        ans += 1
if ans == n:
    print(-1)
else:
    print(ans)