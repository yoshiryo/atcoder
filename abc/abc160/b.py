x = int(input())
cnt1 = x//500
x -= 500*cnt1
cnt2 = x//5
print(cnt1*1000 + cnt2*5)