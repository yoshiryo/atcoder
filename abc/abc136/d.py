s = input()
cnt_r = 0
cnt_l = 0
p = 0
ans = [0]*len(s)
for i in range(len(s)):
    if p == 0:
        if s[i] == "R":
            cnt_r += 1
        else:
            lp = i
            cnt_l += 1
            p = 1
    else:
        if s[i] == "L":
            cnt_l += 1
        else:
            p = 0
            if cnt_r%2 == 0:
                ans[lp] += cnt_r//2
                ans[lp-1] += cnt_r//2
            else:
                ans[lp] += cnt_r//2
                ans[lp-1] += cnt_r//2 + 1
            if cnt_l%2 == 0:
                ans[lp] += cnt_l//2
                ans[lp-1] += cnt_l//2
            else:
                ans[lp] += cnt_l//2 + 1
                ans[lp-1] += cnt_l//2
            cnt_r = 1
            cnt_l = 0
if cnt_r%2 == 0:
    ans[lp] += cnt_r//2
    ans[lp-1] += cnt_r//2
else:
    ans[lp] += cnt_r//2
    ans[lp-1] += cnt_r//2 + 1
if cnt_l%2 == 0:
    ans[lp] += cnt_l//2
    ans[lp-1] += cnt_l//2
else:
    ans[lp] += cnt_l//2 + 1
    ans[lp-1] += cnt_l//2

print(*ans)