s = input()
for i in range(len(s)):
    if (i+1)%2 == 1:
        if s[i] in ["R", "U", "D"]: continue
        print("No")
        exit()
    else:
        if s[i] in ["L", "U", "D"]: continue
        print("No")
        exit()
print("Yes")