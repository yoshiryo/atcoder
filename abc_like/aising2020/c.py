n = int(input())
ans = [0]*(10**4 + 1)
for x in range(1, 10**2 + 1):
    for y in range(1, 10**2 + 1):
        for z in range(1, 10**2 + 1):
            cnt = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if cnt <= n:
                ans[cnt] += 1
for i in range(1, n+1):
    print(ans[i])
