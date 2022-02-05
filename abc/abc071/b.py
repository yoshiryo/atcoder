s = input()
alp = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alp)):
    if alp[i] not in s:
        print(alp[i])
        exit()
print("None")