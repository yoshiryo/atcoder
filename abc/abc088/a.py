n = int(input())
a = int(input())
cnt = n//500
if cnt*500 + a >= n:
    print("Yes")
else:
    print("No")