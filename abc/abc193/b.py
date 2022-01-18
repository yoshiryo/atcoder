n = int(input())
cnt = 0
m = 10**10
for _ in range(n):
    a, p, x = map(int, input().split())
    if a < x:
        cnt += 1
        m = min(m, p)
if cnt == 0:
    print(-1)
else:
    print(m)
