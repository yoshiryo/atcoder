n = int(input())
all = []
for i in range(n):
    s, p = input().split()
    p = int(p)
    all.append([s, p, i+1])
all = sorted(all, key = lambda x: (x[0], -x[1]))
for ans in all:
    print(ans[2])