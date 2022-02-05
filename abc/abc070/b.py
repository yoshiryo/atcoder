a, b, c, d = map(int, input().split())
ac = max(a, c)
bd = min(b, d)
if ac >= bd:
    print(0)
else:
    print(bd - ac)