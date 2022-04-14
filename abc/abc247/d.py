from collections import deque

q = int(input())
deq = deque()
for _ in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        x, c = que[1:]
        deq.append([x, c])
    else:
        c = que[1]
        su = 0
        while c > 0:
            num, cnt = deq[0]
            if c >= cnt:
                su += num*cnt
                deq.popleft()
                c -= cnt
            else:
                su += num*c
                deq[0][1] -= c
                c = 0
        print(su)
