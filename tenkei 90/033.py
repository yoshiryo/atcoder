h, w = map(int, input().split())
if h == 1 or w == 1:
    print(h*w)
else:   
    if h%2 == 0:
        h_cnt = h//2
    else:
        h_cnt = h//2 + 1
    if w%2 == 0:
        w_cnt = w//2
    else:
        w_cnt = w//2 + 1

    print(h_cnt * w_cnt)