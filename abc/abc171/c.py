n = int(input())
alp = "abcdefghijklmnopqrstuvwxyz"
ans = ""
while True:
    n -= 1
    cnt = n%26
    ans += alp[cnt]
    n //= 26
    if n <= 0:
        break
print(ans[::-1])

