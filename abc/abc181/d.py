from collections import Counter
s = input()
cnt = Counter(s)
if len(s) == 1:
    if int(s)%8 == 0:
        print("Yes")
    else:
        print("No")
elif len(s) == 2:
    if int(s)%8 == 0 or int(s[::-1])%8 == 0:
        print("Yes")
    else:
        print("No")
else:
    for x in range(104, 1000, 8):
        cnt_current = Counter(str(x))
        ok = True
        for key, val in cnt_current.items():
            if val > cnt[key]:
                ok = False
        if ok:
            print("Yes")
            exit()
    print("No")