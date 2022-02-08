s = input()
l = s.split("+")
n = len(l)
ans = 0
for i in range(n):
    if l[i].count("0") == 0:
        ans += 1
print(ans)