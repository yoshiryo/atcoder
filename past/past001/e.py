n, q = map(int, input().split())
ans = [["N"]*n for _ in range(n)]
for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        a, b = s[1:]
        ans[a-1][b-1] = "Y"
    elif s[0] == 2:
        a = s[1]
        l = []
        for i in range(n):
            if ans[i][a-1] == "Y":
                ans[a-1][i] = "Y"
    else:
        a = s[1]
        l = []
        for i in range(n):
            if ans[a-1][i] == "Y":
                for j in range(n):
                    if ans[i][j] == "Y" and j != a-1:
                        l.append(j)
        for i in range(len(l)):
            ans[a-1][l[i]] = "Y"
for i in ans:
    print("".join(i))
