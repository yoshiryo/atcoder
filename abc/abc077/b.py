n = int(input())
for i in range(1, 10**5):
    if i**2 > n:
        print((i-1)**2)
        exit()