p = list(map(int, input().split()))
alpha = "abcdefghijklmnopqrstuvwxyz"
ans = ""
for i in range(26):
    ans += alpha[p[i] - 1]
print(ans)