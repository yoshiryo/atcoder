n = int(input())
s = input()
k = int(input())
judge = s[k-1]
ans = ""
for i in range(n):
    if judge == s[i]:
        ans += judge
    else:
        ans += "*"
print(ans)