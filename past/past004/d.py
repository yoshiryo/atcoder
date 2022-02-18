n = int(input())
s = input()
cnt_list = []
cnt = 0
for i in range(n):
    if s[i] == "#":
        cnt_list.append(cnt)
        cnt = 0
    else:
        cnt += 1
cnt_list.append(cnt)
ans1 = cnt_list[0]
ans2 = max(cnt_list[-1], max(cnt_list) - ans1)
print(ans1, ans2)