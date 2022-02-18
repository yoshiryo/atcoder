n = int(input())
if n == 0:
    print(0)
else:
    l = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""
    while n > 0:
        index = n%36
        ans += l[index]
        n //= 36
    print(ans[::-1])