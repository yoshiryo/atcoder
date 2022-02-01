s = input()
k = int(input())
cnt = 0
for i in range(len(s)):
    if s[i] == "1":
        cnt += 1
    else:
        ans = s[i]
        break
if cnt >= k:
    print(1)
else:
    print(ans)
