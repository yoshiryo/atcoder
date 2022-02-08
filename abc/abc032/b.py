s = input()
k = int(input())
ans = set()
for i in range(len(s) - k + 1):
    pw = s[i:i+k]
    ans.add(pw)
print(len(ans))