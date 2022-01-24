n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
route = []
np = 1
check = [-1]*n
while True:
    if check[np-1] != -1:
        if cnt > k:
            print(route[k])
            break
        else:
            roupe_cnt = cnt - check[np-1]
            ans = route[check[np-1] + (k-cnt)%roupe_cnt]
            print(ans)
            break
    check[np-1] = cnt
    cnt += 1
    route.append(np)
    np = a[np-1]
