k = int(input())
ans = ""
p = 1
while k > 1:
    if k%2 == 0:
        ans += "0"
    else:
        ans += "2"
    k //= 2
print("2" + ans[::-1])