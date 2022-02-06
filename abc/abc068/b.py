n = int(input())
mi = 0
ans = 1
for i in range(1, n+1):
    now = i
    cnt = 0
    while True:
        if now%2 == 0:
            cnt += 1
            now //= 2
        else:
            break
    if mi < cnt:
        ans = i
        mi = cnt
print(ans)