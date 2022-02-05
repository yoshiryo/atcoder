from itertools import product
num = input()
l = list(product([False, True], repeat=3))
for i in l:
    cnt = int(num[0])
    ans = num[0]
    for j in range(3):
        if i[j]:
            cnt += int(num[j+1])
            ans += "+" + num[j+1]
        else:
            cnt -= int(num[j+1])
            ans += "-" + num[j+1]
    if cnt == 7:
        print(ans + "=7")
        exit()