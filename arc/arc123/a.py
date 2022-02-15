a, b, c = map(int,input().split())
t = 2 * b - a - c
if t >= 0:
    ans = t
else:
    if abs(t) % 2 == 0:
        ans = abs(t) // 2
    else:
        ans = (abs(t) + 1) // 2 + 1
print(ans)