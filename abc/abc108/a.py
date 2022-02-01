k = int(input())
cnt1 = 0
cnt2 = 0
for i in range(1, k+1):
    if i%2 == 0:
        cnt1 += 1
    else:
        cnt2 += 1
print(cnt1*cnt2)