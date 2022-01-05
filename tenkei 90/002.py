from itertools import product

n = int(input())
L = list(product([False, True], repeat=n))
ANS = []
for i in range(len(L)):
    l = L[i]
    l_cnt = 0
    r_cnt = 0
    ans = ""
    judge = True
    for j in range(n):
        if l[j]:
            l_cnt += 1
            ans += "("
        else:
            r_cnt += 1
            ans += ")"
        if l_cnt < r_cnt:
            judge = False
            break
    if judge and l_cnt == r_cnt:
        ANS.append(ans)
ANS.sort()
for a in ANS:
    print(a)