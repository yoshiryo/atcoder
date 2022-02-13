x, y, z = map(int, input().split())
for i in range(1, 10**6 + 1):
    if y/x <= i/z:
        print(i-1)
        exit()