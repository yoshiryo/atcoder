h = int(input())
ans = 0
mon = 1
while h > 0:
    h //= 2
    ans += mon
    mon *= 2
print(ans)