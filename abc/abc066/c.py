from collections import deque
n = int(input())
a = list(map(int, input().split()))
d = deque()
for i in range(n):
    if i%2 == 0:
        d.append(a[i])
    else:
        d.appendleft(a[i])
if n%2 == 0:
    print(*list(d))
else:
    print(*list(d)[::-1])