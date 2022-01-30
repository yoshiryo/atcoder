l, r = map(int, input().split())
if r - l >= 2019:
    ans = 0
else:
    ans = 10**10
    for i in range(l, r):
        for j in range(i+1, r+1):
            a = ((i%2019) * (j%2019)) % 2019
            ans = min(ans, a) 
print(ans)