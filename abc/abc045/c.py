from itertools import product
s = input()
L = list(product([False, True], repeat=len(s)-1))
ans = 0
for l in L:
    cnt = 0
    num_s = s[0]
    for i in range(len(s)-1):
        if l[i]:
            num_s += "+" + s[i+1]
        else:
            num_s += s[i+1]
    num = num_s.split("+")
    for i in range(len(num)):
        cnt += int(num[i])
    ans += cnt
print(ans)