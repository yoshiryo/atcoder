n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ans = 10**9

for i in  range(n):
    for j in range(n):
        if i == j:
            time = ab[i][0] + ab[i][1]
        else:
            time = max(ab[i][0], ab[j][1])
        ans = min(ans, time)
print(ans) 