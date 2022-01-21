from itertools import product
n = input()
l = list(product([False, True], repeat=len(n)))
keta = len(n)
ans = 18
for a in l:
    cnt = 0
    su = 0
    for i in range(len(n)):
        if a[i]:
            su += int(n[i])
        else:
            cnt += 1
    if cnt == keta:
        continue
    if su%3 == 0:
        ans = min(ans, cnt)
if ans == 18:
    print(-1)
else:
    print(ans)
