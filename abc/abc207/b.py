a, b, c, d = map(int, input().split())

blue = a
red = 0
ans = 0
if b >= c*d:
    print(-1)
else:
    while True:
        ans += 1
        blue += b
        red += c
        if blue <= red*d:
            break
    print(ans)