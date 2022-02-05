from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
l1 = []
l2 = []
for k, val in c.items():
    if val >= 2:
        l1.append(k)
    if val >= 4:
        l2.append(k)
l1.sort(reverse=True)
l2.sort(reverse=True)
if len(l1) >= 2 and len(l2) > 0:
    print(max(l1[0] * l1[1], l2[0]**2))
elif len(l1) >= 2:
    print(l1[0] * l1[1])
elif len(l2) > 0:
    print(l2[0]**2)
else:
    print(0)