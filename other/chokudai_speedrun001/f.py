n = int(input())
a = list(map(int, input().split()))
ans = 0
mi = -1000000000000000000
for x in a:
    if mi < x:
        ans += 1
        mi = x
print(ans)