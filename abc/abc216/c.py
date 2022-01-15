n = int(input())
ans = ""
while n > 1:
    if n%2 == 0:
        n //= 2
        ans += "B"
    else:
        n -= 1
        ans += "A"
ans += "A"
ans = list(ans)
nans = ans[::-1]
print("".join(nans))