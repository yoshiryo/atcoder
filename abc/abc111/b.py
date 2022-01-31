n = int(input())
for i in range(n,1000):
    s = list(str(i))
    if len(set(s)) == 1:
        print(i)
        exit()