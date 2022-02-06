h, w = map(int, input().split())
a = [input() for _ in range(h)]
ans = ["#"*(w+2)]
for i in range(h):
    s = "#"
    for j in range(w):
        s += a[i][j]
    s += "#"
    ans.append(s)
ans.append("#"*(w+2))
for i in ans:
    print(i)