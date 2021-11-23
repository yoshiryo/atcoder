n, q = map(int, input().split())
next = [-1]*(n+1)
pre = [-1]*(n+1)
for _ in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        next[que[1]] = que[2]
        pre[que[2]] = que[1]
    elif que[0] == 2:
        next[que[1]] = -1
        pre[que[2]] = -1
    else:
        ans = []
        now = que[1]
        while pre[now]!= -1:
            now = pre[now]
        while now != -1:
            ans.append(now)
            now = next[now]
        
        print(len(ans), *ans)
