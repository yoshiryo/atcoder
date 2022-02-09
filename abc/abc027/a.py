from collections import Counter
l = list(map(int, input().split()))
if len(set(l)) == 1:
    print(l[0])
else:
    c = Counter(l)
    for k, val in c.items():
        if val == 1:
            print(k)
            exit()