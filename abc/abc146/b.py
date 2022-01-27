n = int(input())
s = input()
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
for i in range(len(s)):
    index = alp.find(s[i])
    ans += alp[(index + n)%26]
print(ans)