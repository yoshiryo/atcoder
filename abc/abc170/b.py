x, y = map(int, input().split())
for i in range(101):
    for j in range(101):
        if 2*i + 4*j == y and i + j == x:
            print("Yes")
            exit()
print("No")