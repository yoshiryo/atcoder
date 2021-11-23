s = input()
ans = [s]

for i in range(len(s)-1):
    t = s[1:] + s[0]
    ans.append(t)
    s = t
ans.sort()

print(ans[0])
print(ans[len(ans) - 1])
