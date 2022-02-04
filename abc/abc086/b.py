a, b = input().split()
ab = int(a+b)
for i in range(1000):
    if i**2 == ab:
        print("Yes")
        exit()
print("No")