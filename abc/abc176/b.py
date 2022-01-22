n = input()
su = 0
for num in n:
    su += int(num)
if su%9 == 0:
    print("Yes")
else:
    print("No")