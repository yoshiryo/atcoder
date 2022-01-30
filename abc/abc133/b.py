n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        y = x[i]
        z = x[j]
        dis = 0
        for k in range(d):
            dis += (y[k] - z[k])**2
        dis = dis**0.5
        if dis.is_integer():
            ans += 1
print(ans)
