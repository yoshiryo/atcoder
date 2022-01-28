n = int(input())
s = input()
ans = ""
now = s[0]
for i in range(1, n):
    if now == s[i]:
        continue
    ans += now
    now = s[i]
ans += now
print(len(ans))