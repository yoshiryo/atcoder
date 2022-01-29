n = int(input())
a = list(map(int, input().split()))
all = 1
for i in range(n):
    all *= a[i]
su = 0
for i in range(n):
    su += all//a[i]
print(all/su)