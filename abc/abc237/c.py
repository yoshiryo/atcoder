s = input()
ns = s[::-1]
cnt1 = 0
cnt2 = 0
for i in range(len(s)):
    if s[i] == "a":
        cnt1 += 1
    else:
        break
for i in range(len(s)):
    if ns[i] == "a":
        cnt2 += 1
    else:
        break

if cnt2 == 0:
    if s == ns:
        print("Yes")
    else:
        print("No")
else:
    if s == ns:
        print("Yes")
    else:
        if cnt1 >= cnt2:
            print("No")
        else:
            t = s[cnt1:-1*cnt2]
            if t == t[::-1]:
                print("Yes")
            else:
                print("No")
