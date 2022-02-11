s = input()
if len(s) == 1:
    if s == "a":
        print(-1)
    else:
        print("a")
else:
    print("a"*(len(s) - 1))