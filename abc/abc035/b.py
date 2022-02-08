s = input()
t = int(input())
dx = abs(s.count("L") - s.count("R"))
dy = abs(s.count("U") - s.count("D"))
cnt = s.count("?")
if t == 1:
    print(dx + dy + cnt)
else:
    if dx + dy <= cnt:
        if (dx + dy - cnt)%2 == 0:
            print(0)
        else:
            print(1)
    else:
        print(dx + dy - cnt)