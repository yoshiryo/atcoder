n = int(input())
p = list(map(int, input().split()))
l = list(range(1, n+1))
cnt = 0
ans = 0
for i in range(n):
    if p[i] == l[i]:
        cnt += 1
    elif cnt >= 1:
        if cnt == 1:
            ans += 1
            cnt = 0
        elif cnt%2 == 0:
            ans += cnt//2
            cnt = 0
        else:
            ans += cnt//2 + 1
            cnt = 0

if cnt == 1:
    ans += 1
elif cnt%2 == 0:
    ans += cnt//2
else:
    ans += cnt//2 + 1

print(ans)