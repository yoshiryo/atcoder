n = int(input())
if n%1000 == 0:
    print(0)
else:
    cnt = n//1000 + 1
    print(1000*cnt - n)