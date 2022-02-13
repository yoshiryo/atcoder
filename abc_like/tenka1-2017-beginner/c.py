N = int(input())
for h in range(1, 3501):
    for n in range(1, 3501):
        d = 4*h*n - N*(h+n)
        if d <= 0:
            continue
        w = (N*h*n)/d
        if w.is_integer() and 0 <= w <= 3500:
            print(h, n, int(w))
            exit()