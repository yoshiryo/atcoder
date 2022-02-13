a, b, c, d = map(int, input().split())
ma = max(a, c)
mi = min(b, d)
if ma <= mi:
    print("Yes")
else:
    print("No")