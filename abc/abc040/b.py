n = int(input())
ans = 10**10
for i in range(1, 10**5 + 1):
    j = n//i
    diff = abs(i - j)
    re = n - i*j
    ans = min(ans, diff + re)
print(ans)