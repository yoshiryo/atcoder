from collections import deque
n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
lim = (n-1)//2
d = deque()
d.append(min(a))
l = 1
r = n-1
cnt = 0
judge = True
while cnt < lim:
    cnt += 1
    if judge:
        d.appendleft(a[r])
        r -= 1
        d.append(a[r])
        r -= 1
        judge = False
    else:
        d.append(a[l])
        l += 1
        d.appendleft(a[l])
        l += 1
        judge = True
re = a[l]
if abs(re - d[0]) > abs(re - d[-1]):
    d.appendleft(re)
else:
    d.append(re)
d = list(d)
ans = 0
for i in range(n-1):
    ans += abs(d[i+1] - d[i])
print(ans)