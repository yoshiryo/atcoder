n = int(input())
ans = []
for _ in range(n):
    s = input()
    cnt = 0
    for i in range(len(s)):
        if s[i] == "0":
            cnt += 1
        else:
            break
    if len(s) == cnt:
        ans.append([0, cnt, s])
    else:
        ans.append([int(s[cnt:]), cnt, s])
ans = sorted(ans, key=lambda x:(x[0], -1*x[1]))
for _, _, i in ans:
    print(i)