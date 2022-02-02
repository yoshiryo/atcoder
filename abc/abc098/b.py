n = int(input())
s = list(input())
ans = 0
for i in range(n):
    X = s[:i]
    Y = s[i:]
    X = list(set(X))
    cnt = 0
    for x in X:
        if x in Y:
            cnt += 1
    ans = max(ans, cnt)
print(ans)