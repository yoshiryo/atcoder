import math
n = int(input())
a = list(map(int, input().split()))
all = 0
cnt = 0
for i in range(n):
    if a[i] != 0:
        cnt += 1
        all += a[i]
print(math.ceil(all/cnt))