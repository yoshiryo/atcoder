n = int(input())
sp = []
all = 0
for _ in range(n):
    s, p = input().split()
    p = int(p)
    all += p
    sp.append([s, p])
for name, num in sp:
    if num > all/2:
        print(name)
        exit()
print("atcoder")