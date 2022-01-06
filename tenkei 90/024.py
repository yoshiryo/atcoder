n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
su = 0
for i in range(n):
    diff = abs(a[i] - b[i])
    su += diff
if su > k:
    print("No")
else:
    if k%2 == su%2:
        print("Yes")
    else:
        print("No")