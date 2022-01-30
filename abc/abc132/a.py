s = input()
ns = set(list(s))
if len(ns) == 2:
    ns = list(ns)
    s1 = ns[0]
    s2 = ns[1]
    if s.count(s1) == 2 and s.count(s2) == 2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
