n = int(input())
s = [input() for _ in range(n)]
ans = []
for i in range(n):
    t = ""
    for j in range(n):
        t += s[j][i]
    t = t[::-1]
    ans.append(t)
for i in ans:
    print(i)