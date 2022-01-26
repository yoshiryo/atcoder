s = input()
n = len(s)
mid = n//2
ls = s[:mid]
rs = s[mid+1:]
if s == s[::-1] and ls == ls[::-1] and rs == rs[::-1]:
    print("Yes")
else:
    print("No")