n = int(input())
a = list(map(int, input().split()))
ans = 10**10
for y in range(-1000, 1001):
    cnt = 0
    for x in a:
        cnt += (x-y)**2
    ans = min(ans, cnt)
print(ans)