sa = input()
sb = input()
sc = input()
cnt = [len(sa), len(sb), len(sc)]
now = 1
while True:
    if now == 1:
        if cnt[0] == 0:
            print("A")
            exit()
        next = sa[0]
        sa = sa[1:]
        cnt[0] -= 1
    elif now == 2:
        if cnt[1] == 0:
            print("B")
            exit()
        next = sb[0]
        sb = sb[1:]
        cnt[1] -= 1
    else:
        if cnt[2] == 0:
            print("C")
            exit()
        next = sc[0]
        sc = sc[1:]
        cnt[2] -= 1
    if next == "a":
        now = 1
    elif next == "b":
        now = 2
    else:
        now = 3