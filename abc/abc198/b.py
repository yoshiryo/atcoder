n = input()
for i in range(10):
    ns = "0"*i + n
    if ns == ns[::-1]:
        print("Yes")
        exit()
print("No")