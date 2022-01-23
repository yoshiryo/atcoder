x, n = map(int, input().split())
p = list(map(int, input().split()))
diff = 1000
ans = 0
for i in range(-10000, 10000):
    judge = True
    for j in range(n):
        if i == p[j]:
            judge = False
            break
    if judge:
        if diff > abs(x - i):
            ans = i
            diff = abs(x - i)
print(ans)
