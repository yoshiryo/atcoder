s = list(input())
l = len(s)
cnt1 = s[2:l-1].count("C")
cnt2 = 0
for i in range(l):
    if s[i].isupper():
        cnt2 += 1
if s[0] == "A" and cnt1 == 1 and cnt2 == 2:
    print("AC")
else:
    print("WA")