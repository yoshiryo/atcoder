c = [list(input().split()) for _ in range(4)]
ans = []
for i in range(3, -1, -1):
    t = c[i]
    ans.append(t[::-1])
for i in ans:
    print(*i)