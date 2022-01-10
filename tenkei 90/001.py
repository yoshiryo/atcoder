n, l = map(int, input().split())
k = int(input())
a = [0] + list(map(int, input().split()))
a.append(l)
def check(d):
    cnt = 0
    l = 0
    for i in range(n+1):
        l += a[i+1] - a[i]
        if l >= d:
            cnt += 1
            l = 0
    return cnt >= k+1
ng = l
ok = -1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)