n = int(input())
s = input()
l = 0
r = s.count(".")
ans = r
for i in range(n):
    if s[i] == "#":
        l += 1
    else:
        r -= 1
    ans = min(ans, l + r)
print(ans)