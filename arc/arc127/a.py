n = int(input())
ans = 0
for i in range(1, 16):
    for j in range(16):
        l = int("1"*i + "0"*j)
        if n < l:
            continue
        r = int("1"*(i-1) + "2" + "0"*j)
        r = min(r, n+1)
        ans += r - l
print(ans)