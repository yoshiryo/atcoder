n = int(input())
a = list(map(int, input().split()))
mid = a[0]
a.sort()
cnt1 = 0
cnt2 = 0
for i in range(len(a)):
    if a[i] != -1 and mid > a[i]:
        cnt1 += 1
    if a[i] != -1 and mid < a[i]:
        cnt2 += 1
if cnt1 < n and cnt2 < n:
    print("Yes")
else:
    print("No")