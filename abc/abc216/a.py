xy = input()
x, y = xy.split(".")

if 0 <= int(y) <= 2:
    print(x + "-")
elif 3 <= int(y) <= 6:
    print(x)
else:
    print(x + "+")