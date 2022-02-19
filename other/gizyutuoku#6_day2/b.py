n = int(input())
s = list(input())
t = list(input())
cnt = 0
for i in range(n-1):
    if s[i] != t[i]:
        if s[i] != s[i+1]:
            print(-1)
            exit()
        else:
            s[i] = t[i]
            s[i+1] = t[i]
            cnt += 1
if s == t:
    print(cnt)
else:
    print(-1)