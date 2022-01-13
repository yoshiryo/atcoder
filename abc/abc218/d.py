from collections import defaultdict

n = int(input())
xy = []
judge = defaultdict(int)
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])
    judge[(x, y)] = 1
ans = 0

for i in range(n-1):
    for j in range(i + 1, n):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        if x1 == x2 or y1 == y2:
            continue
        if judge[(x1, y2)] == 1 and judge[(x2, y1)] == 1:
            ans += 1
ans //= 2
print(ans)