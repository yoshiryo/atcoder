n = int(input())
a = list(map(int, input().split()))
cnt = [0]
now = 0
for i in range(n):
    now += a[i]
    cnt.append(now%360)
cnt.sort()
cnt.append(360)
ans = 0
for i in range(len(cnt)-1):
    ans = max(ans, cnt[i+1] - cnt[i])
print(ans)