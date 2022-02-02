n = int(input())
s = input()
cnt_e = s.count("E")
cnt_w = 0
ans = float("inf")
for i in range(n):
    if s[i] == "E":
        cnt_e -= 1
        ans = min(ans, cnt_e + cnt_w)
    else:
        cnt_w += 1
        ans = min(ans, cnt_e + cnt_w - 1)

print(ans)