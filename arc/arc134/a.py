n, l, w = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    if a[i+1] - a[i] > w:
        d = a[i+1] - (a[i] + w)
        ans += (d + w - 1)//w
if a[0] != 0:
    ans += (a[0] + w - 1)//w
if a[-1] + w < l:
    d = l - (a[-1] + w)
    ans += (d + w - 1)//w
print(ans)
