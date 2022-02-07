cnt = list(map(int, input().split()))
cnt.sort()
if cnt[0] + cnt[1] == cnt[2]:
    print("Yes")
else:
    print("No")