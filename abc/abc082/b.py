from collections import Counter

s = Counter(input())
t = Counter(input())
ns = sorted(s.items())
nt = sorted(t.items(), reverse=True)
S = ""
T = ""
for i in range(len(ns)):
    S += ns[i][0] * ns[i][1]
for i in range(len(nt)):
    T += nt[i][0] * nt[i][1]

if S < T:
    print("Yes")
else:
    print("No")