n, k = map(int, input().split())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
ab = sorted(ab, key=lambda x:x[0])
cnt = 0
for i in range(n):
    cnt += ab[i][1]
    if cnt >= k:
        print(ab[i][0])
        exit()