n = int(input())
a = list(map(int, input().split()))
cnt_4 = 0
cnt_2 = 0
cnt_1 = 0
for i in range(n):
    if a[i]%4 == 0:
        cnt_4 += 1
    elif a[i]%2 == 0:
        cnt_2 += 1
    else:
        cnt_1 += 1
if cnt_2 == 0:
    if (cnt_1-1) <= cnt_4:
        print("Yes")
    else:
        print("No")
else:
    if cnt_1 <= cnt_4:
        print("Yes")
    else:
        print("No")