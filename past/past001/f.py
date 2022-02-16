s = input()
judge = True
t1 = ""
t2 = ""
all = []
for i in range(len(s)):
    if judge and s[i].isupper():
        judge = False
        t1 += s[i]
        t2 += s[i]
    elif not judge and s[i].isupper():
        judge = True
        t1 += s[i]
        t2 += s[i]
        t1 = t1.upper()
        all.append([t1, t2])
        t1 = ""
        t2 = ""
    else:
        t1 += s[i]
        t2 += s[i]
all = sorted(all, key=lambda x:x[0])
ans = ""
for i in range(len(all)):
    ans += all[i][1]
print(ans)