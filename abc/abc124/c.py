s = list(input())
n = len(s)
ans = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        if s[i+1] == "0":
            s[i+1] = "1"
            ans += 1
        else:
            s[i+1] = "0"
            ans += 1

print(ans)