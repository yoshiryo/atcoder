s = input()
now = s[0]
cnt = 1
for i in range(1, len(s)):
    if now == s[i]:
        cnt += 1
    else:
        if cnt >= 3:
            print(now)
            exit()
        else:
            now = s[i]
            cnt = 1
if cnt >= 3:
    print(now)
else:
    print("draw")
