x = int(input())
cnt = x//11

if x%11 == 0:
    print(cnt*2)
elif x%11 <= 6:
    print(cnt*2 + 1)
else:
    print(cnt*2 + 2)