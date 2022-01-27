n = int(input())
s = input()
if n%2 != 0:
    print("No")
else:
    mid = n//2
    l = s[:mid]
    r = s[mid:]
    if l == r:
        print("Yes")
    else:
        print("No")