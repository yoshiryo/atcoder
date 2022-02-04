n = input()
num = int(n)
n = list(n)
su = sum([int(i) for i in n])
if num%su == 0:
    print("Yes")
else:
    print("No")
