n, k, m = map(int, input().split())
a = list(map(int, input().split()))
all = sum(a)
for score in range(k+1):
    if (all + score)/n >= m:
        print(score)
        exit()
print(-1)