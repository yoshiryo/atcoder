a, b, x = map(int, input().split())
l = 0
r = 10**9 + 1
while r - l > 1:
    mid = (l + r)//2
    if a*mid + b*len(str(mid)) <= x:
        l = mid
    else:
        r = mid
print(l)