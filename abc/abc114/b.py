s = input()
n = len(s)
ans = 10**10
for i in range(n-2):
    num = int(s[i:i+3])
    ans = min(ans, abs(num - 753))
print(ans)
