import math
n = int(input())
mi = 0
ma = 10**10
for _ in range(n):
    l, r = map(int, input().split())
    ma = min(ma, r)
    mi = max(mi, l)
    if mi <= ma:
        print(0)
    else:
        tmp = math.ceil(abs(mi - ma)/2)
        print(tmp)