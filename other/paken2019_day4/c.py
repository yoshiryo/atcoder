lr = [list(map(int, input().split())) for _ in range(3)]
ans = 0
for i in range(lr[0][0], lr[0][1] + 1):
    now = 1
    for j in range(1, 3):
        if lr[j][0] <= i:
            now *= max(lr[j][1] - i, 0)/(lr[j][1] - lr[j][0] + 1)
    ans += now/(lr[0][1] - lr[0][0] + 1)
print(ans)