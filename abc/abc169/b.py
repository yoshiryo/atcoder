n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 1
for num in a:
    if num == 0:
        ans = 0
        break
    ans *= num
    if ans > 10**18:
        ans = -1
        break
print(ans)