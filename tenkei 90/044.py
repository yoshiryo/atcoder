n, q = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for _ in range(q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        x_index = (x - cnt)%n
        y_index = (y - cnt)%n
        a[x_index], a[y_index] = a[y_index], a[x_index]
    elif t == 2:
        cnt += 1
    else:
        print(a[x - cnt])