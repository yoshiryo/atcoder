n, k = map(int, input().split())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
ab = sorted(ab, key=lambda x:(x[0], x[1]))
now = 0
for i in range(n):
    diff = ab[i][0] - now
    if k >= diff:
        k -= diff
        k += ab[i][1]
        now = ab[i][0]
    else:
        print(now + k)
        exit()
print(now+k)