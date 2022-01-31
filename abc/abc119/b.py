n = int(input())
ans = 0
for _ in range(n):
    x, u = input().split()
    if u == "JPY":
        ans += int(x)
    else:
        x = float(x)
        ans += x*380000
print(ans)