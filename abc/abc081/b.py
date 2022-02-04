n = int(input())
a = list(map(int, input().split()))
ans = 10**10
for i in range(n):
    cnt = 0
    while a[i]%2 == 0:
        cnt += 1
        a[i] //= 2
    ans = min(ans, cnt)
print(ans)