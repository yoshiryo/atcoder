n = int(input())
x = list(map(int, input().split()))
ans = 10**10
for i in range(-100, 110):
    su = 0
    now = i
    for j in range(n):
        su += (x[j] - now)**2
    ans = min(ans, su)
print(ans)