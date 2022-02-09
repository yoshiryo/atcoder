n = int(input())
a = list(map(int, input().split()))
all = sum(a)
if all%n != 0:
    print(-1)
else:
    goal = all//n
    ans = 0
    l = 0
    r = 0
    while l < n:
        r += 1
        su = sum(a[l:r])
        diff = r - l
        if su%diff == 0 and su//diff == goal:
            l = r
        else:
            ans += 1
    print(ans)
