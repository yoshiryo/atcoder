n = int(input())
s = input()
t = ""
for i in range(n):
    if s[i] in t:
        t = t.replace(s[i], "")
        t += s[i]
    else:
        t += s[i]
print(t)