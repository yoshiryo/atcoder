x = int(input())
re = x%100
if re == 0:
    print(1)
else:
    cnt = x//100
    if 0 <= re <= 5*cnt:
        print(1)
    else:
        print(0)