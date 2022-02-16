n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    cnt = 1
    now = a[i]
    while i+1 != now:
        cnt += 1
        now = a[now-1]
    ans.append(cnt)
print(*ans)