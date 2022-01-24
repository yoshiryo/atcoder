n = input()
s = int(n[-1])
h = [2, 4, 5, 7, 9]
p = [0, 1, 6, 8]
if s in h:
    print("hon")
elif s in p:
    print("pon")
else:
    print("bon")
