def f(x):
    if x%2 == 0:
        return x//2
    else:
        return 3*x + 1

s = int(input())
all = set()
all.add(s)
for i in range(1, 1000001):
    ns = f(s)
    if ns in all:
        print(i+1)
        exit()
    all.add(ns)
    s = ns
