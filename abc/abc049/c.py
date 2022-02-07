s = input()
s = s[::-1]
i = 0
while i < len(s):
    if s[i] == "m":
        if s[i:i+5] != "maerd":
            print("NO")
            exit()
        else:
            i += 5
    elif s[i] == "e":
        if s[i:i+5] != "esare":
            print("NO")
            exit()
        else:
            i += 5
    elif s[i:i+3] == "rem":
        if s[i:i+7] != "remaerd":
            print("NO")
            exit()
        else:
            i += 7
    elif s[i:i+3] == "res":
        if s[i:i+6] != "resare":
            print("NO")
            exit()
        else:
            i += 6
    else:
        print("NO")
        exit()

print("YES")    
