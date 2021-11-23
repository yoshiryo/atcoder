s = input()
t = input()


if s == t:
    print("Yes")
else:
    for i in range(len(s)-1):
        ns = list(s)
        ns[i], ns[i+1] = ns[i+1], ns[i]
        if "".join(ns) == t:
            print("Yes")
            exit()
    print("No")