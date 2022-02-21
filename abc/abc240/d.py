n = int(input())
a = list(map(int, input().split()))
all = []
cnt = 0
for i in range(n):
    cnt += 1
    if len(all) != 0 and all[-1][0] == a[i]:
        all[-1][1] += 1
    else:
        all.append([a[i], 1])
    if all[-1][0] == all[-1][1]:
        cnt -= all[-1][0]
        all.pop()
    print(cnt)
