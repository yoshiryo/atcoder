s = input()
O = []
X = []
for i in range(10):
    if s[i] == "o":
        O.append(str(i))
    if s[i] == "x":
        X.append(str(i))
ans = 0
for i in range(10000):
    judge = True
    num = str(i).zfill(4)
    for o in O:
        if o not in num:
            judge = False
    for x in X:
        if x in num:
            judge = False
    if judge:
        ans += 1
print(ans)