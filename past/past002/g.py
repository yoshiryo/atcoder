from collections import deque
q = int(input())
dq = deque()
for _ in range(q):
    t = input().split()
    if t[0] == "1":
        c = t[1]
        x = int(t[2])
        dq.append((c, x))
    else:
        d = int(t[1])
        a = [0]*26
        while len(dq) > 0 and d > 0:
            c, x = dq.popleft()
            if d <= x:
                a[ord(c) - ord("a")] += d
                dq.appendleft((c, x - d))
                d = 0
            else:
                d -= x
                a[ord(c)-ord('a')] += x
        ans = 0
        for i in a:
            ans += i**2
        print(ans)