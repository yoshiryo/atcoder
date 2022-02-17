from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
cnt = []
mid = s[n//2][0]
for i in range(n):
    c = Counter(sorted(s[i]))
    cnt.append(c)
ans = ""
for i in range(n//2):
    judge = False
    l = []
    for k, _ in cnt[n-i-1].items():
        l.append(k)
    for k, _ in cnt[i].items():
        if k in l:
            judge = True
            ans += k
            break
    if not judge:
        print(-1)
        exit()
if n%2 == 1:
    ans = ans + mid + ans[::-1]
else:
    ans = ans + ans[::-1]
print(ans)
    