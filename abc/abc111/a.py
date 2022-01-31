s = list(input())
for i in range(len(s)):
    if s[i] == "1":
        s[i] = "9"
    elif s[i] == "9":
        s[i] = "1"
    else:
        continue
print("".join(s))
