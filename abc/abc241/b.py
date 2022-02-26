from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c1 = Counter(a)
c2 = Counter(b)
for k2, v2 in c2.items():
    if c1[k2] >= v2:
        c1[k2] -= v2
    else:
        print("No")
        exit()
print("Yes")