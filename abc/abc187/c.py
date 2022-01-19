n = int(input())
s1 = []
s2 = []
for _ in range(n):
    s = input()
    if s[0] == "!":
        s2.append(s[1:])
    else:
        s1.append(s)
s1 = set(s1)
s2 = set(s2)

for s in s1:
    if s in s2:
        print(s)
        exit()
print("satisfiable")