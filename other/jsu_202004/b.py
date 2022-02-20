n = int(input())
r = []
b = []
for _ in range(n):
    x, c = input().split()
    x = int(x)
    if c == "R":
        r.append(x)
    else:
        b.append(x)
r.sort()
b.sort()
for i in r:
    print(i)
for i in b:
    print(i)