N, M, Q = map(int,input().split())
score = [N] * M
solved = [[] for _ in range(N)]
for _ in range(Q):
    s = list(input().split())
    if s[0] == "2":
        n = int(s[1])
        m = int(s[2])
        n -= 1
        m -= 1
        solved[n].append(m)
        score[m] -= 1
    else:
        n = int(s[1])
        n -= 1
        ans = 0
        for t in solved[n]:
            ans += score[t]
        print(ans)