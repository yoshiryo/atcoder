n = int(input())
a = list(map(int, input().split()))
su = 0
minus_cnt = 0
zero_cnt = 0
mi = 10**9
for i in range(n):
    su += abs(a[i])
    mi = min(mi, abs(a[i]))
    if a[i] < 0:
        minus_cnt += 1

if minus_cnt%2 == 0:
    print(su)
else:
    print(su-mi*2)