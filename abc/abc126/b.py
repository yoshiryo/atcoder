s = input()
l = int(s[:2])
r = int(s[2:])
if 1 <= l <= 12 and 1 <= r <= 12:
    print("AMBIGUOUS")
elif 1 <= l <= 12:
    print("MMYY")
elif 1 <= r <= 12:
    print("YYMM")
else:
    print("NA")