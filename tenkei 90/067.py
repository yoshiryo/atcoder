def base10to(n, b):
    if n // b:
        return base10to(n // b, b) + str(n % b)
    return str(n % b)

n, k = input().split()
for _ in range(int(k)):
    num10 = int(n, 8)
    num9 = base10to(num10, 9)
    n = ""
    for i in range(len(num9)):
        if num9[i] == "8":
            n += "5"
        else:
            n += num9[i]
print(n)

