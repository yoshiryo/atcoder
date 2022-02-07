n, x = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(n-1):
    if a[i]+a[i+1] > x:
        num = a[i]+a[i+1]-x
        cnt += num
        if a[i+1] < num:
            a[i+1] = 0
        else:
            a[i+1] -= num
print(cnt)