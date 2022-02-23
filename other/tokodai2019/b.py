import re
n = int(input())
for _ in range(n):
    s = input()
    if re.fullmatch(".*okyo.*ech.*", s):
        print("Yes")
    else:
        print("No")