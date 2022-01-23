from bisect import bisect_right

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_sum = [0]
b_sum = [0]
su = 0
for i in range(n):
    su += a[i]
    a_sum.append(su)
su = 0
for i in range(m):
    su += b[i]
    b_sum.append(su)
ans = 0
for i in range(n+1):
    time = k - a_sum[i]
    if time < 0:
        break
    cnt1 = i
    cnt2 = bisect_right(b_sum, time) - 1
    cnt = cnt1 + cnt2
    ans = max(ans, cnt)
print(ans)