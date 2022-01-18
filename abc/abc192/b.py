s = input()

for i in range(len(s)):
    if i%2 == 0:
        if not s[i].islower():
            print("No")
            exit()
    else:
        if not s[i].isupper():
            print("No")
            exit()
print("Yes")