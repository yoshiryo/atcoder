n, a, b = map(int, input().split())
ans = 0
for i in range(1, n+1):
    s = list(str(i))
    su = sum([int(j) for j in s])
    if a <= su <= b:
        ans += i
print(ans)
