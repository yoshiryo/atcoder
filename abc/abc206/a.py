n = int(input())
n *= 1.08

if int(n) < 206:
    print("Yay!")
elif int(n) == 206:
    print("so-so")
else:
    print(":(")