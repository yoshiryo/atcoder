d = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 10**10
money = 0
for i in range(d):
    money += a[i]
    if money >= b[i]:
        ans = min(ans, b[i])
if ans == 10**10:
    print(-1)
else:
    print(ans)