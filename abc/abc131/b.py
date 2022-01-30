n, l = map(int, input().split())
all = 0
ans = 10**10
for i in range(n):
    a = l + i 
    all += a
    if ans > abs(a):
        ans = abs(a)
        now = a
print(all - now)