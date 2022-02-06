n = int(input())
a = list(map(int, input().split()))
rate = [0]*8
top = 0
for i in range(n):
    if a[i]//400 >= 8:
        top += 1
    else:
        rate[a[i]//400] = 1
cnt = rate.count(1)
if cnt == 0:
    print(1, cnt+top)
else:
    print(cnt, cnt+top)
