s = input()
cnt = 1
now = s[0]
ans = ""
for i in range(1, len(s)):
    if now == s[i]:
        cnt += 1
    else:
        ans += s[i-1] + str(cnt)
        cnt = 1
        now = s[i]
ans += s[-1] + str(cnt)
print(ans)