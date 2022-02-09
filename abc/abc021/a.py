n = int(input())
s = format(n, 'b')
s = s[::-1]
ans = []
for i in range(len(s)):
    if s[i] == "1":
        ans.append(2**i)
print(len(ans))
for i in ans:
    print(i)