n = int(input())
a = list(map(int, input().split()))
now = a[0]
cnt = 1
ans = 0
for i in range(1, n):
    if now < a[i]:
        cnt += 1
        now = a[i]
    else:
        ans += cnt*(cnt+1)//2
        cnt = 1
        now = a[i]
ans += cnt*(cnt+1)//2
print(ans)