import itertools
num = list(map(int, input().split()))
all = itertools.combinations('01234', 3)
ans = []
for part in all:
    cnt = 0
    for i in part:
        cnt += num[int(i)]
    ans.append(cnt)
ans.sort()
print(ans[-3])