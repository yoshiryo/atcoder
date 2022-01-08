n = int(input())
s = input()
cnt = 0
l = []
for i in range(n-1):
    cnt += 1
    if s[i] != s[i+1]:
        l.append(cnt)
        cnt = 0
cnt += 1
l.append(cnt)
su = 0
for i in range(len(l)):
    su += l[i]*(l[i] + 1) // 2
all = n*(n+1) // 2
print(all - su)