m, n, k = map(int, input().split())
X = list(map(int, input().split()))

C = [0 for _ in range(m + 1)]
for i in range(n):
    C[X[i]] += 1
ans = 1
for i in range(1, m + 1):
    temp = C[i]
    D = [False for _ in range(k + 1)]
    for j in range(1, m + 1):
        if i == j:
            continue
        d = abs(i - j)
        if d <= k and C[j] > 0 and not D[d]:
            D[d] = True
            temp += 1
    ans = max(ans, temp)
print(ans)
