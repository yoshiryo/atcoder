n, x = map(int, input().split())
a = list(map(int, input().split()))
all = 0
for i in range(n):
    if i%2 == 1:
        all += a[i] - 1
    else:
        all += a[i]
if all <= x:
    print("Yes")
else:
    print("No")