txa, tya, txb, tyb, t, v = map(int, input().split())
n = int(input())
ma = t*v
for _ in range(n):
    x, y = map(int, input().split())
    da = (x - txa)**2 + (y - tya)**2
    da **= 0.5
    db = (txb - x)**2 + (tyb - y)**2
    db **= 0.5
    if da + db <= ma:
        print("YES")
        exit()
print("NO")