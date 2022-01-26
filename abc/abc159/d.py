from collections import Counter
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    elif r < 0: return 0
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
k = list(c.keys())
all = 0

for i in range(len(c)):
    all += cmb(c[k[i]], 2)

for i in range(n):
    ans = all
    ans = ans - c[a[i]]*(c[a[i]]-1)//2 + (c[a[i]]-1)*(c[a[i]]-2)//2
    print(ans)