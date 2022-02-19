n = int(input())
ans = []
for i in range(n):
    k = int(input())
    s = list(input().split())
    if i == 0:
        for name in s:
            ans.append(name)
    else:
        t = []
        for j in range(len(ans)):
            if ans[j] in s:
                t.append(ans[j])
        ans = t
print(len(ans))
