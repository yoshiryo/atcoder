n = int(input())
all = [i for i in range(2, 2*n+2)]
print(1)
for _ in range(n+1):
    m = int(input())
    if m == 0:
        exit()
    else:
        all.remove(m)
    print(all[0])
    all.pop(0)