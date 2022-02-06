o = input()
e = input()
ans = ""
o_cnt = 0
e_cnt = 0
for i in range(len(o) + len(e)):
    if i%2 == 0:
        ans += o[o_cnt]
        o_cnt += 1
    else:
        ans += e[e_cnt]
        e_cnt += 1
print(ans)