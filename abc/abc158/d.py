from collections import deque
s = input()
q = int(input())
d = deque()
for i in range(len(s)):
  d.append(s[i])
judge = True
for _ in range(q):
    que = list(input().split())
    t = int(que[0])
    if t == 1:
        if judge:
            judge = False
        else:
            judge = True
    else:
        f, c = int(que[1]), que[2]
        if f == 1:
            if judge:
                d.appendleft(c)
            else:
                d.append(c)
        else:
            if judge:
                d.append(c)
            else:
                d.appendleft(c)
ans = "".join(list(d))
if judge:
    print(ans)
else:
    print(ans[::-1])