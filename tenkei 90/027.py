n = int(input())
name = set()
for i in range(n):
    s = input()
    t1 = len(name)
    name.add(s)
    t2 = len(name)
    if t1 != t2:
        print(i+1)