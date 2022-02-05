s = input()
t = input()
l = []
for i in range(len(s)-len(t)+1):
    ans = ""
    cnt = 0
    for j in range(len(t)):
        if s[i+j] == "?" or s[i+j] == t[j]:
            cnt += 1
    p = 0
    if cnt == len(t):
        for k in range(len(s)):
            if i <= k and k <= j+i:
                ans += t[p]
                p += 1
            else:
                if s[k] == "?":
                    ans += "a"
                else:
                    ans += s[k]
    if len(ans) != 0:
        l.append(ans)
l = sorted(l, reverse=True)
if len(l) == 0:
    print("UNRESTORABLE")
else:
    print(l[len(l)-1])